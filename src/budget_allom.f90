! Copyright 2023- LabTerra

!     This program is free software: you can redistribute it and/or modify
!     it under the terms of the GNU General Public License as published by
!     the Free Software Foundation, either version 3 of the License, or
!     (at your option) any later version.

!     This program is distributed in the hope that it will be useful,
!     but WITHOUT ANY WARRANTY; without even the implied warranty of
!     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
!     GNU General Public License for more details.

!     You should have received a copy of the GNU General Public License
!     along with this program.  If not, see <http://www.gnu.org/licenses/>.

! contacts :: David Montenegro Lapola <lapoladm ( at ) gmail.com>
! Author: Bianca Rius and JP Darela
! This program is based on the work of those that gave us the INPE-CPTEC-PVM2 model

! This program is a modified version of budget1. It is being developed to desconsider
! nutri cycle for allocation and to implement allocation following allometric restrictions

module budget_allom
   implicit none
   private
 
   public :: daily_budget_allom
 
contains
 
   subroutine daily_budget_allom(dt, w1, w2, wmax_in, ts, temp, p0, ipar, rh, catm&
      &, cleaf_in, cwood_in, croot_in, cheart_in, csap_in&
      &, dleaf_in, dwood_in, droot_in, dsap_in, dheart_in&
      &, evavg, epavg, phavg, aravg, nppavg, laiavg, rcavg&
      &, f5avg, rmavg, rgavg, wueavg, cueavg, vcmax_1&
      &, specific_la_1, ocpavg)

      use types
      use global_par, only: ntraits, npls
      use alloc
      use productivity
      use omp_lib

      use photo, only: pft_area_frac, sto_resp
      use water, only: evpot2, penman, available_energy, runoff
      use alloc2

      !==========================================================================
      !     ----------------------------INPUTS-------------------------------

      !PLS traits (traits)
      real(r_8),dimension(ntraits,npls),intent(in) :: dt

      !Vegetation pools
      real(r_8),dimension(npls),intent(in) :: cleaf_in
      real(r_8),dimension(npls),intent(in) :: cwood_in
      real(r_8),dimension(npls),intent(in) :: croot_in
      real(r_8),dimension(npls),intent(in) :: cheart_in
      real(r_8),dimension(npls),intent(in) :: csap_in

      !Delta vegetation pools
      real(r_8),dimension(npls),intent(in) :: dleaf_in
      real(r_8),dimension(npls),intent(in) :: dwood_in
      real(r_8),dimension(npls),intent(in) :: droot_in
      real(r_8),dimension(npls),intent(in) :: dheart_in
      real(r_8),dimension(npls),intent(in) :: dsap_in

      !Water
      real(r_8),intent(in) :: w1  !Initial (previous month last day) soil moisture storage (mm) - upper layer
      real(r_8),intent(in) :: w2  !Initial (previous month last day) soil moisture storage (mm) - lower layer

      !Soil
      real(r_4),intent(in) :: ts      ! Soil temperature (oC)
      real(r_8),intent(in) :: wmax_in ! Saturation point

      !Climatic data
      real(r_4),intent(in) :: temp    ! Surface air temperature (oC)
      real(r_4),intent(in) :: p0      ! Surface pressure (mb)
      real(r_4),intent(in) :: ipar    ! Incident photosynthetic active radiation mol Photons m-2 s-1
      real(r_4),intent(in) :: rh      ! Relative humidity 
      real(r_8),intent(in) :: catm    ! ATM CO2 concentration ppm


      !==========================================================================

      !==========================================================================
      !     ----------------------------OUTPUTS-------------------------------

      !DAILY OUTPUTS
      ! real(r_8),dimension(npls),intent(out) :: cleaf_out
      real(r_8),dimension(npls),intent(out) :: ocpavg    ! [0-1] Gridcell occupation

      !CWM OUTPUTS
      real(r_4),intent(out) :: epavg          !Maximum evapotranspiration (mm/day)
      real(r_8),intent(out) :: evavg          !Actual evapotranspiration Daily average (mm/day)
      real(r_8),intent(out) :: phavg          !Daily photosynthesis (Kg m-2 y-1)
      real(r_8),intent(out) :: aravg          !Daily autotrophic respiration (Kg m-2 y-1)
      real(r_8),intent(out) :: nppavg         !Daily NPP (average between PFTs)(Kg m-2 y-1)
      real(r_8),intent(out) :: laiavg         !Daily leaf19010101', '19551231 area Index m2m-2
      real(r_8),intent(out) :: rcavg          !Daily canopy resistence s/m

      real(r_8),intent(out) :: f5avg          !Daily canopy resistence s/m
      real(r_8),intent(out) :: rmavg          !maintenance/growth respiration (Kg m-2 y-1)
      real(r_8),intent(out) :: rgavg          !maintenance/growth respiration (Kg m-2 y-1)
      real(r_8),intent(out) :: wueavg         ! Water use efficiency
      real(r_8),intent(out) :: cueavg         ! [0-1]
      real(r_8),intent(out) :: vcmax_1          ! µmol m-2 s-1
      real(r_8),intent(out) :: specific_la_1    ! m2 g(C)-1

      !==========================================================================

      !==========================================================================
      !     ---------------------INTERNAL VARIABLES-------------------------------

      !index for PLS loops
      integer(i_4) :: i
      integer(i_4) :: p
      integer(i_4) :: counter
      integer(i_4) :: ri


      !PLSs
      real(r_8),dimension(ntraits) :: dt1 ! Store one PLS attributes array (1D)
      integer(i_4) :: nlen !number of alive PLSs
      integer(i_4), dimension(:), allocatable :: lp ! index of living PLSs/living grasses
      real(r_8), dimension(:), allocatable :: idx_grasses !grass identifier

      !Carbon vegetation pools
      real(r_8),dimension(npls) :: cleaf_pls
      real(r_8),dimension(npls) :: cwood_pls
      real(r_8),dimension(npls) :: croot_pls
      real(r_8),dimension(npls) :: cheart_pls
      real(r_8),dimension(npls) :: csap_pls

      !Delta veg pools
      real(r_8),dimension(npls) :: dleaf
      real(r_8),dimension(npls) :: dwood
      real(r_8),dimension(npls) :: droot
      real(r_8),dimension(npls) :: dheart
      real(r_8),dimension(npls) :: dsap


      !Carbon Cycle
      real(r_4),dimension(:),allocatable :: ph           !Canopy gross photosynthesis (kgC/m2/yr)
      real(r_4),dimension(:),allocatable :: ar           !Autotrophic respiration (kgC/m2/yr)
      real(r_4),dimension(:),allocatable :: nppa         !Net primary productivity / auxiliar
      real(r_8),dimension(:),allocatable :: laia         !Leaf area index (m2 leaf/m2 area)
      real(r_8),dimension(:),allocatable :: f5           !Foliar Photosynthesis (mol/m2/s)
      real(r_4),dimension(:),allocatable :: vpd          !Vapor Pressure deficit
      real(r_4),dimension(:),allocatable :: rm           !Maintenance respiration (kgC/m2/yr)
      real(r_4),dimension(:),allocatable :: rg           !Growth respiration (kgC/m2/yr)
      real(r_4),dimension(:),allocatable :: cue          !Carbon use efficiency
      real(r_4),dimension(:),allocatable :: c_def        !Carbon deficit due to negative NPP (kgC/m2/yr) - i.e. ph < ar
      real(r_8),dimension(:),allocatable :: vcmax        !Rubisco maximum velocity of carboxilation (µmol/m2/s)
      real(r_8),dimension(:),allocatable :: specific_la  !Specific leaf area (m2/kg)
      real(r_8),dimension(:),allocatable :: litter_l     ! leaf litter
      real(r_8),dimension(:),allocatable :: cwd          ! coarse wood debris (to litter)
      real(r_8),dimension(:),allocatable :: litter_fr    ! fine roots litter

      !water pools
      real(r_8) :: w  !Daily soil moisture storage (mm)
      !Water cycle
      real(r_4),dimension(:),allocatable :: evap   !Actual evapotranspiration (mm/day)
      real(r_4),dimension(:),allocatable :: wue    !Water use efficiency
      real(r_4),dimension(:),allocatable :: rc2    !Canopy resistence (s/m)
      real(r_8),dimension(:),allocatable :: tra    !Transpiration (mm/s)
      real(r_4) :: emax                            !Maximum evapotranspiration (mm/day)

      !soil
      real(r_4) :: soil_temp !soil temperature
      real(r_8) :: soil_sat  !soil water saturation point
      
      !area frac occupation
      real(r_8),    dimension(npls) :: awood_aux !define if tree or grass
      logical(l_1), dimension(npls) :: ocp_wood  !wood occupation
      integer(i_4), dimension(npls) :: run       !verifies if the PLS is alive
      real(r_8),    dimension(npls) :: ocp_mm    ! TODO include cabon of dead plssss in the cicle? (not implemented)
      real(r_8),dimension(:),allocatable :: ocp_coeffs !occupancy coefficients for each PLS


      !===========================================================================

      !Initializing

      !ATENÇÃO, VERIFICAR QUESTÃO DO TOTAL WOOD
      
      do i = 1, npls
         awood_aux(i) = dt(7,i)

         cleaf_pls(i)  = cleaf_in(i)
         cwood_pls(i)  = cwood_in(i)
         croot_pls(i)  = croot_in(i)
         cheart_pls(i) = cheart_in(i)
         csap_pls(i)   = csap_in(i)

         dleaf(i)  = dleaf_in(i)
         dwood(i)  = dwood_in(i)
         droot(i)  = droot_in(i)
         dsap(i)   = dsap_in(i)
         dheart(i) = dheart_in(i)
         
         ! cleaf_out(i) = cleaf_pls(i) + 1.
      
      enddo

      w = w1 + w2        
      soil_temp = ts     
      soil_sat = wmax_in

      call pft_area_frac(cleaf_pls, croot_pls, cwood_pls, awood_aux,&
      &                 ocpavg, ocp_wood, run, ocp_mm)

      nlen = sum(run)    ! New length for the arrays in the main loop
                         ! get the total number of alives

      allocate(lp(nlen))
      allocate(ocp_coeffs(nlen))
      allocate(idx_grasses(nlen))

      ! Get only living PLSs
      counter = 1
      do p = 1,npls
         if(run(p).eq. 1) then
            lp(counter) = p
            ocp_coeffs(counter) = ocpavg(p)
            counter = counter + 1
         endif
      enddo
      
      ! Identify grasses
      idx_grasses(:) = 1.0D0
      
      do p = 1, nlen
         if (awood_aux(lp(p)) .le. 0.0D0) idx_grasses(p) = 0.0D0
         !This variable multipies ocp_coeffs for the wood tissues. If it is
         !a grass it turns the ocp_coeffs for wood_tissues = 0
      enddo

      !dimensioning according to alive PLSs
      allocate(evap(nlen))
      allocate(nppa(nlen))
      allocate(ph(nlen))
      allocate(ar(nlen))
      allocate(laia(nlen))
      allocate(f5(nlen))
      allocate(vpd(nlen))
      allocate(rc2(nlen))
      allocate(rm(nlen))
      allocate(rg(nlen))
      allocate(wue(nlen))
      allocate(cue(nlen))
      allocate(c_def(nlen))
      allocate(vcmax(nlen))
      allocate(specific_la(nlen))
      allocate(litter_l(nlen))
      allocate(cwd(nlen))
      allocate(litter_fr(nlen))
      allocate(tra(nlen))

      !     Maximum evapotranspiration (emax)
      !     =================================
      emax = evpot2(p0,temp,rh,available_energy(temp))


      ! FAZER NUmthreads função de nlen pra otimizar a criação de trheads
      if (nlen .le. 20) then
         call OMP_SET_NUM_THREADS(1)
      else if (nlen .le. 100) then
         call OMP_SET_NUM_THREADS(1)
      else if (nlen .le. 300) then
         call OMP_SET_NUM_THREADS(2)
      else if (nlen .le. 600) then
         call OMP_SET_NUM_THREADS(3)
      else
         call OMP_SET_NUM_THREADS(3)
      endif
      !$OMP PARALLEL DO &
      !$OMP SCHEDULE(AUTO) &
      !$OMP DEFAULT(SHARED)

      do p = 1,nlen
         
         ri = lp(p) !get the correspondentt value of for that specific pls (don't lose the original PLS index)
         dt1 = dt(:,ri) ! Pick up the pls functional attributes list
        
         !here ri is real index. The outputs use p to save memory, but at the end of the doc
         !it is transformed in p

         !!!!!!INPUT OF CSAP ONCE IT IS IT THAT RESPIRE?

         
         call prod(dt1, ocp_wood(ri), catm, temp, soil_temp, p0, w, ipar&
            &, rh, emax, cleaf_pls(ri), cwood_pls(ri), croot_pls(ri), dleaf(ri), dwood(ri), droot(ri)&
            &, soil_sat, ph(p), ar(p), nppa(p), laia(p), f5(p), vpd(p)&
            &, rm(p), rg(p), rc2(p), wue(p), c_def(p), vcmax(p), specific_la(p), tra(p))
      
         
         evap(p) = penman(p0, temp, rh, available_energy(temp), rc2(p)) !actual evapotranspiration (evap, mm/day)

         call allocation2(dt1, nppa(p), cleaf_pls(ri), cwood_pls(ri)&
            &, croot_pls(ri), csap_pls(ri), cheart_pls(ri))
         
         !Carbon use efficiency & Delta C
         if(ph(p) .eq. 0.0 .or. nppa(p) .eq. 0.0) then
            cue(p) = 0.0
         else
            cue(p) = nppa(p)/ph(p)
         endif

         !estimate growth of storage pool (acho que isso vai ser dentro da alloc)
         !calculate storage growth respi(onde isso?)

         ! growth_stoc = 0.0D0
         ! mr_sto = 0.0D0
         ! sr = 0.0D0

         !aqui teria que mudar para as suas variáveis
         ! delta_cveg(1,p) = cl2(p) - cl1_pft(ri)  !kg m-2
         ! if(dt1(4) .lt. 0.0D0) then
         !    delta_cveg(2,p) = 0.0D0
         ! else
         !    delta_cveg(2,p) = ca2(p) - ca1_pft(ri)
         ! endif
         ! delta_cveg(3,p) = cf2(p) - cf1_pft(ri)

         !mass balance (acho que vai direto na alloc)     
      enddo
      !$OMP END PARALLEL DO

      epavg = emax

      !Fill output data
      evavg  = 0.0D0
      phavg  = 0.0D0
      aravg  = 0.0D0
      nppavg = 0.0D0
      laiavg = 0.0D0        
      rcavg  = 0.0D0        
      f5avg  = 0.0D0        
      rmavg  = 0.0D0       
      rgavg  = 0.0D0       
      wueavg = 0.0D0       
      cueavg = 0.0D0       
      vcmax_1 = 0.0D0       
      specific_la_1 = 0.0D0  


      ! Calculate CWM for ecosystem processes
 
      ! Filter NaN in ocupation (abundance) coefficients
      do p = 1, nlen
         if(isnan(ocp_coeffs(p))) ocp_coeffs(p) = 0.0D0
      enddo

      evavg  = sum(real(evap, kind=r_8) * ocp_coeffs, mask= .not. isnan(evap))
      phavg  = sum(real(ph, kind=r_8) * ocp_coeffs, mask= .not. isnan(ph))
      aravg  = sum(real(ar, kind=r_8) * ocp_coeffs, mask= .not. isnan(ar))
      nppavg = sum(real(nppa, kind=r_8) * ocp_coeffs, mask= .not. isnan(nppa))
      laiavg = sum(laia * ocp_coeffs, mask= .not. isnan(laia))
      rcavg = sum(real(rc2, kind=r_8) * ocp_coeffs, mask= .not. isnan(rc2))
      f5avg = sum(f5 * ocp_coeffs, mask= .not. isnan(f5))
      rmavg = sum(real(rm, kind=r_8) * ocp_coeffs, mask= .not. isnan(rm))
      rgavg = sum(real(rg, kind=r_8) * ocp_coeffs, mask= .not. isnan(rg))
      wueavg = sum(real(wue, kind=r_8) * ocp_coeffs, mask= .not. isnan(wue))
      cueavg = sum(real(cue, kind=r_8) * ocp_coeffs, mask= .not. isnan(cue))
      vcmax_1 = sum(vcmax * ocp_coeffs, mask= .not. isnan(vcmax))
      specific_la_1 = sum(specific_la * ocp_coeffs, mask= .not. isnan(specific_la))

      deallocate(lp)
      deallocate(evap)
      deallocate(nppa)
      deallocate(ph)
      deallocate(ar)
      deallocate(laia)
      deallocate(f5)
      deallocate(vpd)
      deallocate(rc2)
      deallocate(rm)
      deallocate(rg)
      deallocate(wue)
      deallocate(cue)
      deallocate(c_def)
      deallocate(vcmax)
      deallocate(specific_la)
      deallocate(litter_l)
      deallocate(cwd)
      deallocate(litter_fr)
      deallocate(tra)
      deallocate(idx_grasses)


   end subroutine daily_budget_allom
 
 end module budget_allom
 
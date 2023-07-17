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
 
   subroutine daily_budget_allom(dt, w1, w2, ts, wmax_in&
      &, cleaf_in, cwood_in, croot_in, cheart_in, csap_in&
      &, cleaf_out, ocpavg)

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

      !PLS TABLE (traits)
      real(r_8),dimension(ntraits,npls),intent(in) :: dt

      !VEGETATION POOLS
      real(r_8),dimension(npls),intent(in) :: cleaf_in
      real(r_8),dimension(npls),intent(in) :: cwood_in
      real(r_8),dimension(npls),intent(in) :: croot_in
      real(r_8),dimension(npls),intent(in) :: cheart_in
      real(r_8),dimension(npls),intent(in) :: csap_in

      !WATER
      real(r_8),intent(in) :: w1  !Initial (previous month last day) soil moisture storage (mm) - upper layer
      real(r_8),intent(in) :: w2  !Initial (previous month last day) soil moisture storage (mm) - lower layer

      !SOIL
      real(r_4),intent(in) :: ts      ! Soil temperature (oC)
      real(r_8),intent(in) :: wmax_in ! Saturation point

      !==========================================================================

      !==========================================================================
      !     ----------------------------OUTPUTS-------------------------------

      !DAILY OUTPUTS
      real(r_8),dimension(npls),intent(out) :: cleaf_out
      real(r_8),dimension(npls),intent(out) :: ocpavg    ! [0-1] Gridcell occupation

      !CWM OUTPUTS

      !==========================================================================

      !==========================================================================
      !     ---------------------INTERNAL VARIABLES-------------------------------

      !index for the PLS loop
      integer(i_4) :: i

      !number of alive PLSs
      integer(i_4) :: nlen

      !vegetation pools
      real(r_8),dimension(npls) :: cleaf_pls
      real(r_8),dimension(npls) :: cwood_pls
      real(r_8),dimension(npls) :: croot_pls
      real(r_8),dimension(npls) :: cheart_pls
      real(r_8),dimension(npls) :: csap_pls

      !water pools
      real(r_8) :: w  !Daily soil moisture storage (mm)
      
      !soil
      real(r_4) :: soil_temp !soil temperature
      real(r_8) :: soil_sat  !soil water saturation point
      
      !area frac occupation
      real(r_8),    dimension(npls) :: awood_aux !define if tree or grass
      logical(l_1), dimension(npls) :: ocp_wood  !wood occupation
      integer(i_4), dimension(npls) :: run       !verifies if the PLS is alive
      real(r_8),    dimension(npls) :: ocp_mm    ! TODO include cabon of dead plssss in the cicle? (not implemented)
      !===========================================================================

      !Initializing

      do i = 1, npls
         awood_aux(i) = dt(7,i)

         cleaf_pls(i)  = cleaf_in(i)
         cwood_pls(i)  = cwood_in(i)
         croot_pls(i)  = croot_in(i)
         cheart_pls(i) = cheart_in(i)
         csap_pls(i)   = csap_in(i)

         
         cleaf_out(i) = cleaf_pls(i) + 1.
      
      enddo

      w = w1 + w2        
      soil_temp = ts     
      soil_sat = wmax_in

      call pft_area_frac(cleaf_pls, croot_pls, cwood_pls, awood_aux,&
      &                 ocpavg, ocp_wood, run, ocp_mm)

      nlen = sum(run)    ! New length for the arrays in the main loop
                         ! get the total number of alives

      print*, 'nlen', nlen
   
   end subroutine daily_budget_allom
 
 end module budget_allom
 
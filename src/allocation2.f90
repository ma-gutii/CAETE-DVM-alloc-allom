   ! Copyright 2017- LabTerra

!     This program is free software: you can redistribute it and/or modify
!     it under the terms of the GNU General Public License as published by
!     the Free Software Foundation, either version 3 of the License, or
!     (at your option) any later version.)

!     This program is distributed in the hope that it will be useful,
!     but WITHOUT ANY WARRANTY; without even the implied warranty of
!     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
!     GNU General Public License for more details.

!     You should have received a copy of the GNU General Public License
!     along with this program.  If not, see <http://www.gnu.org/licenses/>.

! AUTHORS: Bianca Rius, Bárbara Cardeli, Carolina Blanco, JP Darela, David Lapola
! contact: <biancafaziorius ( at ) gmail.com>
!
!
! This module was developed to include allometric constraints on carbon distribution
!for plant tissues. It is mainly based on LPJ scheme (Sitch et al. 2003; Smith et al. 2001),
!although some implementations were developed by CAETÊ group.
!We also used LPJ code as reference: LPJ-LMFire.
!You can access a conceptual diagram for this allocation scheme at Bianca Rius' github:
!https://github.com/BiancaRius/CAETE-DVM-alloc-allom

module alloc2

    use types
    use global_par
    
    implicit none
    private

    public:: allocation2

    contains

    subroutine allocation2(npp, scl1, sca1, scf1, scs1, sch1, sct1, &
        scl2, sca2, scf2, scs2, sch2, sct2)

        !inputs
        real(r_4),intent(in) :: npp  ! npp (KgC/m2/yr) gpp (µmol m-2 s)
        real(r_8),intent(in) :: scl1 ! previous day carbon content on leaf compartment (KgC/m2)
        real(r_8),intent(in) :: scf1 ! previous day carbon content on fine roots compartment (KgC/m2)
        real(r_8),intent(in) :: scs1 ! previous day carbon content on sapwood compartment (KgC/m2)
        real(r_8),intent(in) :: sch1 ! previous day carbon content on heartwood compartment (KgC/m2)
        real(r_8),intent(in) :: sct1 ! previous day carbon content on storage compartment (KgC/m2)
        real(r_8),intent(in) :: sca1 ! previous day carbon content on aboveground woody biomass compartment(KgC/m2)
                                     ! sum of sapwood and heartwood


        !outputs
        real(r_8),intent(out) :: scl2 ! final carbon content on leaf compartment (KgC/m2)
        real(r_8),intent(out) :: scf2 ! final carbon content on fine roots compartment (KgC/m2)
        real(r_8),intent(out) :: scs2 ! final carbon content on sapwood compartment (KgC/m2)
        real(r_8),intent(out) :: sch2 ! final carbon content on heartwood compartment (KgC/m2)
        real(r_8),intent(out) :: sct2 ! final carbon content on storage compartment (KgC/m2)
        real(r_8),intent(out) :: sca2 ! final carbon content on aboveground woody biomass compartment (KgC/m2)
                                      ! sum of sapwood and heartwood

        

        !initialize all outputs
        scl2 = 0.0D0
        scf2 = 0.0D0
        sca2 = 0.0D0
        scs2 = 0.0D0
        sct2 = 0.0D0
        sch2 = 0.0D0
  

        print*, 'calling module alloc2'

    end subroutine allocation2

end module alloc2
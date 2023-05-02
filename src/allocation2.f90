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

    subroutine allocation2(bminc_in, leaf_in, wood_in, root_in, sap_in, heart_in, storage_in, dens_in,&
        leaf_out, wood_out, root_out, sap_out, heart_out, storage_out)

        
        !VARIABLE INPUTS

        !carbon inputs (kgC/m2)
        real(r_8), intent(in) :: leaf_in
        real(r_8), intent(in) :: root_in
        real(r_8), intent(in) :: sap_in
        real(r_8), intent(in) :: heart_in
        real(r_8), intent(in) :: storage_in
        real(r_8), intent(in) :: wood_in

        !input of individuals density (ind/m2)
        real(r_8), intent(in) :: dens_in !ind/m2 initial density of individuals

        !input of carbon available gc/m2/time_step
        real(r_4), intent(in) :: bminc_in !carbon (NPP) available to be allocated
                                          !basically NPPt - NPPt-1. NPP accumulated in the year/month/day
                                         
        !VARIABLES OUTPUTS 
        !carbon inputs (kgC/m2)
        real(r_8), intent(out) :: leaf_out
        real(r_8), intent(out) :: root_out
        real(r_8), intent(out) :: sap_out
        real(r_8), intent(out) :: heart_out
        real(r_8), intent(out) :: storage_out
        real(r_8), intent(out) :: wood_out


        !INTERNAL VARIABLES

        !carbon (gC) in compartments considering the density (ind/m2)
        real(r_8) :: leaf_in_ind
        real(r_8) :: root_in_ind
        real(r_8) :: sap_in_ind
        real(r_8) :: heart_in_ind
        real(r_8) :: storage_in_ind
        real(r_8) :: wood_in_ind 


        !carbon available for allocation (gC) considering the density of individuals
        real(r_8) :: bminc_in_ind
        
        !initializing variables
        leaf_in_ind = 0.0D0
        root_in_ind = 0.0D0
        sap_in_ind = 0.0D0
        heart_in_ind = 0.0D0
        wood_in_ind = 0.0D0
        storage_in_ind = 0.0D0

        leaf_out = 0.0D0
        root_out = 0.0D0
        sap_out  = 0.0D0
        heart_out = 0.0D0
        storage_out = 0.0D0
        wood_out = 0.0D0

        print*, 'calling module alloc2'

    end subroutine allocation2

end module alloc2
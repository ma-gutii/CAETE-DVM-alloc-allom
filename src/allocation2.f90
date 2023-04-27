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
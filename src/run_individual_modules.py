import caete_module as ct

leaf_in  = 1.5
root_in  = 1.2
sap_in = 100.
heart_in = 500.
storage_in = 5.
bminc_in = 1.5
dens_in = 10.

leaf_in_ind = (leaf_in/dens_in)*1000.
root_in_ind = (root_in/dens_in)*1000.
sap_in_ind = (sap_in/dens_in)*1000. 
heart_in_ind = (heart_in/dens_in)*1000.
storage_in_ind = (storage_in/dens_in)*1000.
wood_in_ind = sap_in_ind + heart_in_ind

#running a isolated module/function
#ct(como eu chamei o caete_module).alloc2(subrotina para acessar modulo).height_calc(exemplo de função de interesse)(coloque os inputs da função ou módulo)


print(ct.alloc2.height_calc(wood_in_ind))
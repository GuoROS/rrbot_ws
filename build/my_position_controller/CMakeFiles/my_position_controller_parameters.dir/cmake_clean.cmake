file(REMOVE_RECURSE
  "include/my_position_controller/my_position_controller_parameters.hpp"
  "include/my_position_controller_parameters.hpp"
)

# Per-language clean rules from dependency scanning.
foreach(lang )
  include(CMakeFiles/my_position_controller_parameters.dir/cmake_clean_${lang}.cmake OPTIONAL)
endforeach()

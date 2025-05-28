cmake_minimum_required(VERSION 3.15...4.0)
project(MonocularVisualOdometry)
find_package( OpenCV 4.8 REQUIRED )

include_directories( ${OpenCV_INCLUDE_DIRS} )

file (GLOB source
     "src/*.h"
     "src/*.cpp"
)

add_executuble(vo ${source})
target_link_libraries( vo ${OpenCV_LIBS} )
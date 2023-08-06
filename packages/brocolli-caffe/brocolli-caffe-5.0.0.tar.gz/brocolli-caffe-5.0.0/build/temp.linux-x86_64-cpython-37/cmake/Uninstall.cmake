if(NOT EXISTS "/root/bro-caffe/build/temp.linux-x86_64-cpython-37/install_manifest.txt")
  message(FATAL_ERROR "Cannot find install manifest: /root/bro-caffe/build/temp.linux-x86_64-cpython-37/install_manifest.txt")
endif(NOT EXISTS "/root/bro-caffe/build/temp.linux-x86_64-cpython-37/install_manifest.txt")

if (NOT DEFINED CMAKE_INSTALL_PREFIX)
  set (CMAKE_INSTALL_PREFIX "/root/bro-caffe/build/temp.linux-x86_64-cpython-37/install")
endif ()
 message(${CMAKE_INSTALL_PREFIX})

file(READ "/root/bro-caffe/build/temp.linux-x86_64-cpython-37/install_manifest.txt" files)
string(REGEX REPLACE "\n" ";" files "${files}")
foreach(file ${files})
  message(STATUS "Uninstalling $ENV{DESTDIR}${file}")
  if(IS_SYMLINK "$ENV{DESTDIR}${file}" OR EXISTS "$ENV{DESTDIR}${file}")
    exec_program(
      "/root/miniconda3/envs/caffe37/bin/cmake" ARGS "-E remove \"$ENV{DESTDIR}${file}\""
      OUTPUT_VARIABLE rm_out
      RETURN_VALUE rm_retval
      )
    if(NOT "${rm_retval}" STREQUAL 0)
      message(FATAL_ERROR "Problem when removing $ENV{DESTDIR}${file}")
    endif(NOT "${rm_retval}" STREQUAL 0)
  else(IS_SYMLINK "$ENV{DESTDIR}${file}" OR EXISTS "$ENV{DESTDIR}${file}")
    message(STATUS "File $ENV{DESTDIR}${file} does not exist.")
  endif(IS_SYMLINK "$ENV{DESTDIR}${file}" OR EXISTS "$ENV{DESTDIR}${file}")
endforeach(file)

// module_a.h
#ifndef MODULE_A_H
#define MODULE_A_H

#ifdef _WIN32
  #define MODULEA_EXPORT __declspec(dllexport)
#else
  #define MODULEA_EXPORT
#endif

void MODULEA_EXPORT hello_a();

#endif // MODULE_A_H
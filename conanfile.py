from conans import ConanFile, CMake, tools


class ModuleAConan(ConanFile):
    name = "module_a"
    version = "0.1"
    license = "ford"
    author = "terickso"
    url = "https://github.com/ford-innersource/lib.cdp.module_a"
    description = "A simple C library"
    settings = "os", "compiler", "build_type", "arch"
    generators = "cmake"

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def package(self):
        self.copy("*.a", dst="lib", src="lib") 
        self.copy("*.lib", dst="lib", src="lib") 
        self.copy("*.dll", dst="bin", src="bin") 
        self.copy("*.so", dst="lib", src="lib") 
        self.copy("*.dylib", dst="lib", src="lib") 
        self.copy("*.h", dst="include") 

    def package_info(self):
        self.cpp_info.libs = ["my_c_library"]
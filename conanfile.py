from conan import ConanFile
from conan.tools.cmake import CMakeToolchain, CMake, cmake_layout, CMakeDeps

class ModuleAConan(ConanFile):
    name = "module_a"
    version = "0.1"
    license = "ford"
    author = "terickso"
    url = "https://github.com/ford-innersource/lib.cdp.module_a"
    description = "A simple C library"
    settings = "os", "compiler", "build_type", "arch"
    exports_sources = "CMakeLists.txt", "src/*", "include/*"
    package_type = "shared-library"
    languages = "C"  # Important to remove compiler.cppstd/compiler.libcxx from config

    def layout(self):
        cmake_layout(self)
    
    def generate(self):
        deps = CMakeDeps(self)
        deps.generate()
        tc = CMakeToolchain(self)
        tc.generate()

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def package(self):
        cmake = CMake(self)
        cmake.install()

    def package_info(self):
        self.cpp_info.libs = ["module_a"]
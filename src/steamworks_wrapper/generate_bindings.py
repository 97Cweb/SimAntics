import re
import os

# Path to the Steamworks flat header file (relative to current script)
header_file_path = r"steamworks_sdk_161/sdk/public/steam/steam_api_flat.h"
output_file_path = r"steamworks_bindings.py"

# Path to redistributable_bin for libraries
redistributable_bin_path = {
    "Windows": {
        "64bit": r"steamworks_sdk_161/sdk/redistributable_bin/win64/steam_api64.dll",
        "32bit": r"steamworks_sdk_161/sdk/redistributable_bin/steam_api.dll"
    },
    "Linux": {
        "64bit": r"steamworks_sdk_161/sdk/redistributable_bin/linux64/libsteam_api.so",
        "32bit": r"steamworks_sdk_161/sdk/redistributable_bin/linux32/libsteam_api.so"
    }
}

def parse_header(file_path):
    """
    Parses the Steamworks flat header file to extract function declarations.
    """
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), file_path), "r") as f:
        content = f.read()

    # Regex to match function declarations
    pattern = re.compile(
        r"(S_API\s+[\w\s\*]+)\s+(\w+)\(([^)]*)\);"
    )

    functions = []
    for match in pattern.finditer(content):
        return_type, func_name, args = match.groups()
        args = [arg.strip() for arg in args.split(",") if arg.strip()]
        functions.append((return_type, func_name, args))

    return functions

def generate_ctypes_bindings(functions):
    """
    Generates Python ctypes bindings for the extracted functions.
    """
    bindings = ["import ctypes\n", "import platform\n", "import os\n"]

    # Add logic to dynamically load the correct Steamworks library
    bindings.append("# Dynamically locate the Steamworks library\n")
    bindings.append("redistributable_bin_path = {\n")
    bindings.append("    'Windows': {\n")
    bindings.append("        '64bit': r'steamworks_sdk_161/sdk/redistributable_bin/win64/steam_api64.dll',\n")
    bindings.append("        '32bit': r'steamworks_sdk_161/sdk/redistributable_bin/steam_api.dll'\n")
    bindings.append("    },\n")
    bindings.append("    'Linux': {\n")
    bindings.append("        '64bit': r'steamworks_sdk_161/sdk/redistributable_bin/linux64/libsteam_api.so',\n")
    bindings.append("        '32bit': r'steamworks_sdk_161/sdk/redistributable_bin/linux32/libsteam_api.so'\n")
    bindings.append("    }\n")
    bindings.append("}\n\n")

    bindings.append(
        "system = platform.system()\n"
        "architecture = platform.architecture()[0]\n"
        "if system not in redistributable_bin_path or architecture not in redistributable_bin_path[system]:\n"
        "    raise OSError(f'Unsupported platform or architecture: {system} {architecture}')\n"
        "library_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), redistributable_bin_path[system][architecture])\n"
        "if not os.path.exists(library_path):\n"
        "    raise FileNotFoundError(f'Steamworks library not found: {library_path}')\n"
        "steam_lib = ctypes.CDLL(library_path)\n\n"
    )

    for return_type, func_name, args in functions:
        # Map C types to ctypes
        arg_types = []
        for arg in args:
            if "*" in arg:
                arg_types.append("ctypes.c_void_p")  # Simplify pointer types
            else:
                arg_types.append("ctypes.c_int")  # Assume integers for simplicity

        bindings.append(f"# Binding for {func_name}\n")
        bindings.append(f"steam_lib.{func_name}.argtypes = [{', '.join(arg_types)}]\n")
        bindings.append(f"steam_lib.{func_name}.restype = ctypes.c_int\n\n")

    return "\n".join(bindings)

def main():
    # Parse the header file
    functions = parse_header(header_file_path)

    # Generate ctypes bindings
    bindings = generate_ctypes_bindings(functions)

    # Write to output file
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), output_file_path), "w") as f:
        f.write(bindings)

    print(f"Bindings generated and saved to {output_file_path}")

if __name__ == "__main__":
    main()

from timescribe import TimeScribe

if __name__ == "__main__":
    input_path = input("Enter input path: ")
    output_path = input("Enter output path (leave blank for default /output/transcript path): ")
    timescribe = TimeScribe()
    if output_path != "":
        timescribe.transcribe_folder(input_path, output_path)
    else:
        timescribe.transcribe_folder(input_path)
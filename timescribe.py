import os
import torch
import whisper_timestamped as whisper


class TimeScribe:
    def __init__(self, model_size: str = "medium"):

        if torch.cuda.is_available():
            self.device = "cuda"
            print("Using GPU")
        else:
            self.device = "cpu"
            print("Using CPU")

        self.model = whisper.load_model(model_size, self.device)

    def transcribe_folder(self, input_path: str, output_path: str = "./output/transcript") -> None:
        # if output path doesn't exist, create it
        if not os.path.exists(output_path):
            os.makedirs(output_path)
        
        # get all files in input path
        files = os.listdir(input_path)

        # speaker_segments = dict()
        transcript = list()

        # iterate through files
        for file in files:
            # if file is a folder, call this function recursively
            if os.path.isdir(os.path.join(input_path, file)):
                self.transcribe_folder(os.path.join(input_path, file), os.path.join(output_path, file))
            # if file is an audio file, transcribe it
            elif file.endswith(".wav") or file.endswith(".flac"):
                # self.transcribe_file(os.path.join(input_path, file), os.path.join(output_path, file))
                audio = whisper.load_audio(os.path.join(input_path, file))
                result = whisper.transcribe(self.model, audio, language="en", vad=True)
                # speaker_segments[file] = result["segments"]
                for segment in result["segments"]:
                    transcript.append((float(segment["start"]), file, segment["text"]))

            # otherwise, ignore it
            else:
                print(f"Skipping {file}")

        
        # with open(f"{output_path}/data.json", "w") as f:
        #     f.write(json.dumps(speaker_segments, indent=4, ensure_ascii=False))

        transcript.sort(key=lambda a: a[0])
        # write transcript to file in sorted order with timestamps
        with open(f"{output_path}/transcript.txt", "w") as f:
            for segment in transcript:
                f.write(f"[{segment[0]}] {segment[1]}: {segment[2]}\n")

if __name__ == "__main__":
    
    timescribe = TimeScribe()
    timescribe.transcribe_folder("./input")
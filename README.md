# python-video-converter-mp4

Pri requisist:

  -> FFmpeg setup

  -> Python setup
  
# FFmpeg setup

FFmpeg is an open-source command-line tool for audio and video file processing. It comprises a suite of programs and libraries for decoding, encoding, streaming, filtering, and playing various multimedia formats.

FFmpeg supports a variety of video codecs including MPEG-1, MPEG-2, VP8, and H.264, which is currently the most popular video codec. It offers high-quality and efficient compression.

FFmpeg also supports several audio codecs, including MP3, AAC, and PCM. For the best audio quality, we need to use a lossless codec such as PCM. However, lossless codecs result in much larger file sizes.

There are three ways to setup ffmpeg:
  
Option 1: Installing FFmpeg on Mac via Homebrew
  Step 1: Update and Upgrade Homebrew Formulae
  Step 2: Install FFmpeg
  
Option 2: Installing FFmpeg on Mac via MacPorts

Option 3: Installing FFmpeg on Mac Using a Static Build
  Step 1: Download FFmpeg
  Step 2: Extract and Move FFmpeg Binary
  
  
  
# Option 1: Installing FFmpeg on Mac via Homebrew

Package manager installations provide automatic app updates, simplifying the management process. The recommended way to install FFmpeg on macOS is using the Homebrew package manager.

The sections below describe the necessary steps and provide three ways to install the tool with Homebrew.

# Step 1: Update and Upgrade Homebrew Formulae

1. Before installing FFmpeg, ensure that Homebrew formulae on the system are up to date:

    brew update


2. Upgrade outdated formulae by running:

    brew upgrade



# Step 2: Install FFmpeg

1. Install the latest version of FFmpeg available on Homebrew with the command below.

    brew install ffmpeg

Homebrew installs the tool and all the dependencies.



2. Wait for the installation to finish, then verify it by launching FFmpeg:

    ffmpeg


If successfully installed, FFmpeg displays an overview of configuration options.

# Option 2: Installing FFmpeg on Mac via MacPorts

MacPorts is another popular package manager for macOS. If you do not have MacPorts on the system, install it by downloading and executing the PKG file for your macOS version.

1. Install FFmpeg on MacPorts by typing the following command:

    sudo port install ffmpeg

2. When prompted, enter Y to proceed with the installation. MacPorts installs FFmpeg and its dependencies.

# Option 3: Installing FFmpeg on Mac Using a Static Build
Another way to install FFmpeg on Mac is to download a static build binary. Static builds allow you to choose and install the latest snapshots and releases. However, app management will be more difficult as you will need to manually update the app.

Follow the steps below to run a static build of FFmpeg.

# Step 1: Download FFmpeg
1. Visit the official FFmpeg download page.

2. In the Get packages & executable files section, select the Apple logo and click the Static builds for macOS 64-bit link.

![image](https://user-images.githubusercontent.com/51235527/236664798-e26768a8-5f3c-4da9-b840-de2e3a96ba7f.png)


3. Scroll down to the FFmpeg section and choose a version. To download the latest snapshot, select Download as ZIP in the column on the left side.

![image](https://user-images.githubusercontent.com/51235527/236664805-260d669e-95d0-4ba4-a469-51ec1c85d623.png)


# Step 2: Extract and Move FFmpeg Binary
When the download completes, execute the following steps to place the binary in a location where the OS will recognize it.

1. Double-click to unzip if the file did not unzip automatically.

2. Move the file to a directory of your choice. Make a note of the directory path.

3. In the terminal, add the directory to the path variable. For example, if the FFmpeg binary is in /Users/test/local, type:

export PATH=$PATH:/Users/test/Local

4. Test the installation by invoking FFmpeg from the terminal.

    ffmpeg

# Python Setup

The best place to install Python is from the official website.

Go to Python.org and click on the Download button to download the latest version for MacOS.

Go to your download folder and double-click on the python-<version>-macosx.pkg file to start the Python installer.

Go through each of the prompts.

Keep the default install location.

Close and move installer to Trash.



# Important commands:

## Convert .mov to .mp4

    ffmpeg -i demo.mov -vcodec h264 demo.mp4

## Convert .avi to .mp4

    ffmpeg -i input_filename.avi -c:v copy -c:a copy -y output_filename.mp4

## Let’s use the ffmpeg command to convert a sample.mp4 video to AVI format using the H.264 codec:

    ffmpeg -i input_filename.mp4 -c:v libx264 output_filename.avi

## Let’s convert the sample.mp4 video to AVI format and convert the audio to PCM format:

    ffmpeg -i input_filename.mp4 -c:v copy -c:a pcm_s16le output_filename.avi

We’re using the -c:v option to specify the video codec, and output_filename.avi represents the output video file.

The -c:v copy option copies the video stream without re-encoding it. The -c:a pcm_s16le option converts the audio stream to uncompressed PCM audio with 16-bit depth and little-endian byte order. This ensures the best audio quality possible.


## Putting it all together, we can convert the input_filename.mp4 video file to AVI while converting audio and video codecs:

    ffmpeg -i input_filename.mp4 -c:v libx264 -c:a pcm_s16le output.avi



# References:
  
-> docs.python.org

-> medium.com

-> phoenixnap.com

#include <iostream>
#include <string>
#include <cstdlib> // for system

int main() {
    // Check if yt-dlp is installed
    if (system("yt-dlp --version") != 0) {
        std::cerr << "yt-dlp is not installed or not found in PATH.\n";
        std::cerr << "Please install yt-dlp and ffmpeg first.\n";
        std::cerr << "To install yt-dlp:\n";
        std::cerr << "- On Mac (Homebrew): brew install yt-dlp\n";
        std::cerr << "- With Pip: pip install yt-dlp\n";
        std::cerr << "- Or download from: https://github.com/yt-dlp/yt-dlp\n";
        std::cerr << "To install ffmpeg (needed for merging):\n";
        std::cerr << "- On Mac (Homebrew): brew install ffmpeg\n";
        std::cerr << "- Or download from: https://ffmpeg.org/download.html\n";
        return 1;
    }

    // Get the YouTube URL from the user
    std::string url;
    std::cout << "Enter the YouTube video URL: ";
    std::getline(std::cin, url);

    // Display download options and get user choice
    std::string choice;
    std::cout << "Select download option:\n";
    std::cout << "1) Download in 720p\n";
    std::cout << "2) Download in the best format available\n";
    std::cout << "Enter your choice (1 or 2): ";
    std::getline(std::cin, choice);

    // Build the yt-dlp command based on the choice
    std::string command;
    if (choice == "1") {
        command = "yt-dlp -f 'bestvideo[height=720]+bestaudio' --merge-output-format mp4 " + url;
        std::cout << "Downloading in 720p...\n";
    } else if (choice == "2") {
        command = "yt-dlp -f 'bestvideo+bestaudio' --merge-output-format mp4 " + url;
        std::cout << "Downloading in the best format available...\n";
    } else {
        std::cerr << "Invalid choice. Please enter 1 or 2.\n";
        return 1;
    }

    // Run the command and check if it succeeds
    int result = system(command.c_str());
    if (result == 0) {
        std::cout << "Video downloaded successfully.\n";
    } else {
        std::cerr << "Error downloading video.\n";
    }

    return 0;
}

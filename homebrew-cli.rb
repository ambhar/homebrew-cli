class HomebrewCli < Formula
  desc "Homebrew add cli"
  homepage "https://github.com/ambhar/homebrew-cli"
  url "https://github.com/ambhar/homebrew-cli/archive/refs/tags/v0.0.2.tar.gz"
  sha256 "9dcddd84d137a9d9855999b6c9c866f2f05cc2a3b211b41be86bf2aab2c3bb3f"
  license "MIT"

  def install
    bin.install "add_cli.py"
  end
end

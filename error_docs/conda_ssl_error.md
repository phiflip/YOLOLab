## Troubleshooting

### Conda SSL Error: OpenSSL Unavailability

**Problem**: Conda is unable to download or install packages because OpenSSL is not available.

**Solution**:
- Navigate to `C:/Users/UserName/Anaconda3/Library/bin`.
- Copy `libcrypto-1_1-x64.dll` and `libssl-1_1-x64.dll`.
- Paste these into `C:/Users/UserName/Anaconda3/DLLs`.
- Restart your PC.

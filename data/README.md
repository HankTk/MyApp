# Data Folder

This folder contains configuration and sample data files used by the application.

## Files

### Configuration Files
- **`app_settings.json`** - Application-wide settings and configuration
- **`user_config.json`** - User-specific configuration and preferences

### Sample Data
- **`sample.json`** - Sample data for demonstration purposes (users, settings, statistics)

## Usage

These files are loaded through the application's JSON loader interface in both the Home and Settings pages. They serve as:

1. **Configuration examples** - Show how to structure configuration data
2. **Demo data** - Provide sample data for testing and demonstration
3. **File loading functionality** - Demonstrate the application's ability to load and edit JSON files

## Loading in Application

The files can be loaded through:
- Home page: JSON Data Loader section
- Settings page: Settings Data Loader section
- Quick load buttons for easy access

## File Structure

All files are in JSON format and follow consistent naming conventions:
- Configuration files: `*_config.json` or `*_settings.json`
- Sample data: `sample.json` 
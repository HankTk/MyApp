// Settings page event handler for NiceGUI application

// Settings form handlers
function handleThemeChange(value) {
    window.parent.postMessage({type: 'theme_change', value: value}, '*');
}

function handleLanguageChange(value) {
    window.parent.postMessage({type: 'language_change', value: value}, '*');
}

function handleNotificationChange(value) {
    window.parent.postMessage({type: 'notification_change', value: value}, '*');
}

function handlePasswordChange() {
    window.parent.postMessage({type: 'password_change'}, '*');
}

function handleAutosaveChange(value) {
    window.parent.postMessage({type: 'autosave_change', value: value}, '*');
}

function handleRetentionChange(value) {
    window.parent.postMessage({type: 'retention_change', value: value}, '*');
}

function handleSaveSettings() {
    const settings = {
        theme: document.getElementById('theme-select')?.value || 'Light',
        language: document.getElementById('language-select')?.value || 'English',
        notifications: document.getElementById('notification-toggle')?.checked || false,
        username: document.getElementById('username-input')?.value || '',
        email: document.getElementById('email-input')?.value || '',
        autosave: document.getElementById('autosave-toggle')?.checked || false,
        retention: document.getElementById('retention-select')?.value || '30 days'
    };
    window.parent.postMessage({type: 'save_settings', settings: settings}, '*');
}

function handleResetSettings() {
    window.parent.postMessage({type: 'reset_settings'}, '*');
}

// Message event listener for settings page
window.addEventListener('message', function(event) {
    const data = event.data;
    
    switch(data.type) {
        case 'theme_change':
            window.parent.postMessage({
                type: 'nicegui_notify',
                message: `Theme changed to: ${data.value}`
            }, '*');
            break;
            
        case 'language_change':
            window.parent.postMessage({
                type: 'nicegui_notify',
                message: `Language changed to: ${data.value}`
            }, '*');
            break;
            
        case 'notification_change':
            window.parent.postMessage({
                type: 'nicegui_notify',
                message: `Notifications: ${data.value ? 'On' : 'Off'}`
            }, '*');
            break;
            
        case 'password_change':
            window.parent.postMessage({
                type: 'nicegui_notify',
                message: 'Password change dialog opened!'
            }, '*');
            break;
            
        case 'autosave_change':
            window.parent.postMessage({
                type: 'nicegui_notify',
                message: `Auto Save: ${data.value ? 'On' : 'Off'}`
            }, '*');
            break;
            
        case 'retention_change':
            window.parent.postMessage({
                type: 'nicegui_notify',
                message: `Data retention changed to: ${data.value}`
            }, '*');
            break;
            
        case 'save_settings':
            window.parent.postMessage({
                type: 'nicegui_notify',
                message: 'Settings saved successfully!'
            }, '*');
            break;
            
        case 'reset_settings':
            window.parent.postMessage({
                type: 'nicegui_notify',
                message: 'Settings reset to default!'
            }, '*');
            break;
            
        default:
            // Let other handlers process this
            break;
    }
});

// Initialize settings handler
console.log('Settings handler loaded and ready'); 
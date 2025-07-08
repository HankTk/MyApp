// Event handler for NiceGUI application
// Handles messages from HTML templates and other components

window.addEventListener('message', function(event) {
    const data = event.data;
    
    switch(data.type) {
        case 'dashboard':
            window.parent.postMessage({
                type: 'nicegui_notify',
                message: 'Dashboard opened!'
            }, '*');
            break;
            
        case 'activity':
            window.parent.postMessage({
                type: 'nicegui_notify',
                message: 'Activity log opened!'
            }, '*');
            break;
            
        case 'quickstart':
            window.parent.postMessage({
                type: 'nicegui_notify',
                message: 'Quick start initiated!'
            }, '*');
            break;
            
        case 'nicegui_notify':
            // Handle notifications from other scripts
            if (window.parent && window.parent.postMessage) {
                window.parent.postMessage({
                    type: 'nicegui_notify',
                    message: data.message,
                    notification_type: data.notification_type || 'info'
                }, '*');
            }
            break;
            
        default:
            console.log('Unhandled message type:', data.type);
            break;
    }
});

// Initialize event handler
console.log('Event handler loaded and ready'); 
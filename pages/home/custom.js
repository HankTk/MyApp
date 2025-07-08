// Custom JavaScript functions for NiceGUI application

// Utility function to show notifications
function showNotification(message, type = 'info') {
    window.parent.postMessage({
        type: 'nicegui_notify',
        message: message,
        notification_type: type
    }, '*');
}

// Function to manipulate DOM elements
function changePageTitle(newTitle) {
    document.title = newTitle;
    showNotification(`Page title changed to: ${newTitle}`);
}

// Function to add custom styles
function addCustomStyle(css) {
    const style = document.createElement('style');
    style.textContent = css;
    document.head.appendChild(style);
    showNotification('Custom styles added');
}

// Function to handle data processing
function processData(data) {
    console.log('Processing data:', data);
    
    // Example data processing
    if (Array.isArray(data)) {
        const processed = data.map(item => ({
            ...item,
            processed: true,
            timestamp: new Date().toISOString()
        }));
        
        showNotification(`Processed ${processed.length} items`);
        return processed;
    }
    
    return data;
}

// Function to create dynamic elements
function createDynamicElement(tag, content, className = '') {
    const element = document.createElement(tag);
    element.textContent = content;
    if (className) {
        element.className = className;
    }
    document.body.appendChild(element);
    showNotification(`Created ${tag} element with content: ${content}`);
}

// Event handler for custom events
function handleCustomEvent(event) {
    console.log('Custom event received:', event);
    showNotification(`Event handled: ${event.type}`);
}

// Initialize custom functionality
function initializeCustomFeatures() {
    console.log('Custom features initialized');
    showNotification('Custom JavaScript loaded and initialized');
    
    // Add event listeners
    document.addEventListener('custom-event', handleCustomEvent);
    
    // Add some default styles
    addCustomStyle(`
        .custom-highlight {
            background-color: #ffeb3b;
            padding: 5px;
            border-radius: 3px;
        }
    `);
}

// Export functions for external use
window.customFunctions = {
    showNotification,
    changePageTitle,
    addCustomStyle,
    processData,
    createDynamicElement,
    handleCustomEvent,
    initializeCustomFeatures
};

// Auto-initialize when script loads
document.addEventListener('DOMContentLoaded', initializeCustomFeatures); 
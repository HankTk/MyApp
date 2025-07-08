// Chart page event handler for NiceGUI application

// Chart data management
let currentChartData = {
    type: 'line',
    x_values: '1,2,3,4,5',
    y_values: '2,4,6,8,10',
    title: 'Sample Line Chart',
    x_label: 'X Axis',
    y_label: 'Y Axis'
};

// Chart type change handler
function handleChartTypeChange(value) {
    currentChartData.type = value;
    window.parent.postMessage({
        type: 'chart_type_change', 
        value: value
    }, '*');
    
    // Update UI based on chart type
    updateUIForChartType(value);
}

// Data change handler
function handleDataChange() {
    currentChartData.x_values = document.getElementById('x-values').value;
    currentChartData.y_values = document.getElementById('y-values').value;
    currentChartData.title = document.getElementById('chart-title').value;
    currentChartData.x_label = document.getElementById('x-label').value;
    currentChartData.y_label = document.getElementById('y-label').value;
    
    window.parent.postMessage({
        type: 'chart_data_change', 
        data: currentChartData
    }, '*');
}

// Generate chart
function generateChart() {
    const chartData = {
        type: document.getElementById('chart-type').value,
        x_values: document.getElementById('x-values').value,
        y_values: document.getElementById('y-values').value,
        title: document.getElementById('chart-title').value,
        x_label: document.getElementById('x-label').value,
        y_label: document.getElementById('y-label').value
    };
    
    window.parent.postMessage({
        type: 'generate_chart', 
        data: chartData
    }, '*');
}

// Reset chart
function resetChart() {
    // Reset to default values
    document.getElementById('chart-type').value = 'line';
    document.getElementById('x-values').value = '1,2,3,4,5';
    document.getElementById('y-values').value = '2,4,6,8,10';
    document.getElementById('chart-title').value = 'Sample Line Chart';
    document.getElementById('x-label').value = 'X Axis';
    document.getElementById('y-label').value = 'Y Axis';
    
    // Clear chart display
    const chartDisplay = document.getElementById('chart-display');
    chartDisplay.innerHTML = `
        <div>
            <h3>📊 Chart Display Area</h3>
            <p>Click "Generate Chart" to create your visualization</p>
        </div>
    `;
    
    window.parent.postMessage({
        type: 'chart_reset'
    }, '*');
}

// Download chart
function downloadChart() {
    const chartImg = document.querySelector('#chart-display img');
    if (chartImg) {
        const link = document.createElement('a');
        link.download = 'chart.png';
        link.href = chartImg.src;
        link.click();
        
        window.parent.postMessage({
            type: 'chart_download'
        }, '*');
    } else {
        window.parent.postMessage({
            type: 'nicegui_notify',
            message: 'No chart to download. Please generate a chart first.'
        }, '*');
    }
}

// Load quick chart
function loadQuickChart(chartType) {
    let xValues, yValues, title;
    
    switch(chartType) {
        case 'line':
            xValues = '1,2,3,4,5';
            yValues = '2,4,6,8,10';
            title = 'Line Chart';
            break;
        case 'bar':
            xValues = 'A,B,C,D,E';
            yValues = '10,20,15,25,30';
            title = 'Bar Chart';
            break;
        case 'scatter':
            xValues = '1,2,3,4,5';
            yValues = '3,1,4,1,5';
            title = 'Scatter Plot';
            break;
        case 'pie':
            xValues = '';
            yValues = '30,20,25,15,10';
            title = 'Pie Chart';
            break;
        case 'random':
            xValues = '1,2,3,4,5,6,7,8,9,10';
            yValues = Array.from({length: 10}, () => Math.floor(Math.random() * 50) + 1).join(',');
            title = 'Random Data Chart';
            break;
        default:
            return;
    }
    
    // Update form fields
    document.getElementById('chart-type').value = chartType;
    document.getElementById('x-values').value = xValues;
    document.getElementById('y-values').value = yValues;
    document.getElementById('chart-title').value = title;
    
    // Update current data
    currentChartData = {
        type: chartType,
        x_values: xValues,
        y_values: yValues,
        title: title,
        x_label: 'X Axis',
        y_label: 'Y Axis'
    };
    
    // Generate chart automatically
    generateChart();
    
    window.parent.postMessage({
        type: 'quick_chart_loaded',
        chart_type: chartType
    }, '*');
}

// Update UI based on chart type
function updateUIForChartType(chartType) {
    const xLabelInput = document.getElementById('x-label');
    const yLabelInput = document.getElementById('y-label');
    
    switch(chartType) {
        case 'pie':
            xLabelInput.disabled = true;
            yLabelInput.value = 'Values';
            break;
        case 'bar':
            xLabelInput.disabled = false;
            yLabelInput.disabled = false;
            xLabelInput.value = 'Categories';
            yLabelInput.value = 'Values';
            break;
        default:
            xLabelInput.disabled = false;
            yLabelInput.disabled = false;
            xLabelInput.value = 'X Axis';
            yLabelInput.value = 'Y Axis';
            break;
    }
}

// Display chart image
function displayChart(imageBase64) {
    const chartDisplay = document.getElementById('chart-display');
    chartDisplay.innerHTML = `
        <img src="data:image/png;base64,${imageBase64}" 
             alt="Generated Chart" 
             style="max-width: 100%; height: auto; border-radius: 8px; box-shadow: 0 4px 15px rgba(0,0,0,0.1);">
    `;
}

// Message event listener for chart page
window.addEventListener('message', function(event) {
    const data = event.data;
    
    switch(data.type) {
        case 'chart_type_change':
            window.parent.postMessage({
                type: 'nicegui_notify',
                message: `Chart type changed to: ${data.value}`
            }, '*');
            break;
            
        case 'chart_data_change':
            window.parent.postMessage({
                type: 'nicegui_notify',
                message: 'Chart data updated'
            }, '*');
            break;
            
        case 'generate_chart':
            window.parent.postMessage({
                type: 'nicegui_notify',
                message: 'Generating chart...'
            }, '*');
            break;
            
        case 'chart_generated':
            if (data.image_base64) {
                displayChart(data.image_base64);
                window.parent.postMessage({
                    type: 'nicegui_notify',
                    message: 'Chart generated successfully!'
                }, '*');
            }
            break;
            
        case 'chart_reset':
            window.parent.postMessage({
                type: 'nicegui_notify',
                message: 'Chart reset to default'
            }, '*');
            break;
            
        case 'chart_download':
            window.parent.postMessage({
                type: 'nicegui_notify',
                message: 'Chart downloaded successfully!'
            }, '*');
            break;
            
        case 'quick_chart_loaded':
            window.parent.postMessage({
                type: 'nicegui_notify',
                message: `Quick ${data.chart_type} chart loaded!`
            }, '*');
            break;
            
        case 'chart_error':
            window.parent.postMessage({
                type: 'nicegui_notify',
                message: `Chart error: ${data.error}`,
                type: 'error'
            }, '*');
            break;
            
        default:
            // Let other handlers process this
            break;
    }
});

// Initialize chart handler
console.log('Chart handler loaded and ready');

// Set up initial UI state
document.addEventListener('DOMContentLoaded', function() {
    updateUIForChartType('line');
}); 
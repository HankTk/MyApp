// Data handling utilities for NiceGUI application

// Data storage object
const DataHandler = {
    // Local storage for data
    storage: {},
    
    // Load data from JSON
    loadFromJSON: function(jsonData) {
        try {
            const data = typeof jsonData === 'string' ? JSON.parse(jsonData) : jsonData;
            this.storage = { ...this.storage, ...data };
            this.notify('Data loaded from JSON');
            return data;
        } catch (error) {
            this.notify('Error loading JSON data: ' + error.message, 'error');
            return null;
        }
    },
    
    // Save data to JSON
    saveToJSON: function(data) {
        try {
            const jsonString = JSON.stringify(data, null, 2);
            this.notify('Data saved to JSON');
            return jsonString;
        } catch (error) {
            this.notify('Error saving to JSON: ' + error.message, 'error');
            return null;
        }
    },
    
    // Filter data
    filterData: function(data, filterCriteria) {
        if (!Array.isArray(data)) {
            this.notify('Data is not an array', 'error');
            return [];
        }
        
        return data.filter(item => {
            return Object.keys(filterCriteria).every(key => {
                if (typeof filterCriteria[key] === 'string') {
                    return item[key] && item[key].toLowerCase().includes(filterCriteria[key].toLowerCase());
                }
                return item[key] === filterCriteria[key];
            });
        });
    },
    
    // Sort data
    sortData: function(data, sortKey, ascending = true) {
        if (!Array.isArray(data)) {
            this.notify('Data is not an array', 'error');
            return [];
        }
        
        return data.sort((a, b) => {
            let aVal = a[sortKey];
            let bVal = b[sortKey];
            
            // Handle numeric values
            if (typeof aVal === 'number' && typeof bVal === 'number') {
                return ascending ? aVal - bVal : bVal - aVal;
            }
            
            // Handle string values
            aVal = String(aVal || '').toLowerCase();
            bVal = String(bVal || '').toLowerCase();
            
            if (ascending) {
                return aVal.localeCompare(bVal);
            } else {
                return bVal.localeCompare(aVal);
            }
        });
    },
    
    // Transform data
    transformData: function(data, transformation) {
        if (!Array.isArray(data)) {
            this.notify('Data is not an array', 'error');
            return [];
        }
        
        return data.map(item => {
            const transformed = {};
            Object.keys(transformation).forEach(key => {
                if (typeof transformation[key] === 'function') {
                    transformed[key] = transformation[key](item);
                } else {
                    transformed[key] = item[transformation[key]];
                }
            });
            return transformed;
        });
    },
    
    // Validate data
    validateData: function(data, schema) {
        const errors = [];
        
        if (Array.isArray(data)) {
            data.forEach((item, index) => {
                const itemErrors = this.validateItem(item, schema);
                if (itemErrors.length > 0) {
                    errors.push({ index, errors: itemErrors });
                }
            });
        } else {
            errors.push(...this.validateItem(data, schema));
        }
        
        if (errors.length > 0) {
            this.notify(`Validation errors found: ${errors.length}`, 'warning');
        } else {
            this.notify('Data validation passed');
        }
        
        return errors;
    },
    
    // Validate individual item
    validateItem: function(item, schema) {
        const errors = [];
        
        Object.keys(schema).forEach(field => {
            const rules = schema[field];
            const value = item[field];
            
            if (rules.required && (value === undefined || value === null || value === '')) {
                errors.push(`${field} is required`);
            }
            
            if (value !== undefined && value !== null) {
                if (rules.type && typeof value !== rules.type) {
                    errors.push(`${field} must be of type ${rules.type}`);
                }
                
                if (rules.minLength && value.length < rules.minLength) {
                    errors.push(`${field} must be at least ${rules.minLength} characters`);
                }
                
                if (rules.maxLength && value.length > rules.maxLength) {
                    errors.push(`${field} must be no more than ${rules.maxLength} characters`);
                }
                
                if (rules.pattern && !rules.pattern.test(value)) {
                    errors.push(`${field} does not match required pattern`);
                }
            }
        });
        
        return errors;
    },
    
    // Export data
    exportData: function(data, format = 'json') {
        switch (format.toLowerCase()) {
            case 'csv':
                return this.exportToCSV(data);
            case 'json':
                return this.saveToJSON(data);
            default:
                this.notify('Unsupported export format: ' + format, 'error');
                return null;
        }
    },
    
    // Export to CSV
    exportToCSV: function(data) {
        if (!Array.isArray(data) || data.length === 0) {
            this.notify('No data to export', 'error');
            return null;
        }
        
        const headers = Object.keys(data[0]);
        const csvContent = [
            headers.join(','),
            ...data.map(row => headers.map(header => `"${row[header] || ''}"`).join(','))
        ].join('\n');
        
        this.notify('Data exported to CSV');
        return csvContent;
    },
    
    // Notification helper
    notify: function(message, type = 'info') {
        window.parent.postMessage({
            type: 'nicegui_notify',
            message: message,
            notification_type: type
        }, '*');
    }
};

// Make DataHandler available globally
window.DataHandler = DataHandler;

// Initialize data handler
console.log('Data Handler loaded and ready');
DataHandler.notify('Data Handler initialized'); 
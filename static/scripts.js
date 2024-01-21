{   // Disable the dropdown if the first (placeholder) option is selected
    document.querySelectorAll('.form-control.dropdown').forEach(function(dropdown) {
        dropdown.addEventListener('change', function() {
            // Disable the dropdown if the first (placeholder) option is selected
            this.disabled = this.selectedIndex === 0;
        });
    });
}

{   // Change text color based on valid selection
    document.addEventListener("DOMContentLoaded", function() {
        var selects = document.querySelectorAll("select.form-control");
    
        // Function to set text color based on the selected option
        function setColorBasedOnSelection(selectElement) {
            selectElement.style.color = selectElement.value === '' ? "#848484" : "#ffffff";
        }
    
        selects.forEach(function(select) {
            // Set initial color
            setColorBasedOnSelection(select);
    
            // Change event listener
            select.addEventListener('change', function() {
                setColorBasedOnSelection(this);
            });
        });
    });
}

{   // Slider Toggle and Value Update: Humidity
    document.addEventListener('DOMContentLoaded', function() {
        // Slider Toggle and Value Update: Humidity
        const humidityVisibleToggle = document.getElementById('humidityVisibleToggle');
        const humidityContainer = document.getElementById('humidityContainer');
        const humiditySlider = document.getElementById('humidity');
        const humidityValue = document.getElementById('humidityValue');
        const humidityValueContainer = document.getElementById('humidityValueContainer'); // Ensure this is the correct ID
    
        humidityVisibleToggle.addEventListener('change', function() {
            if (this.checked) {
                humidityContainer.style.display = 'block'; // Adjust to inline for a single line
                humidityValueContainer.style.display = 'block'; // Show value
                humiditySlider.disabled = false;
                humiditySlider.setAttribute('name', 'humidity'); // Add name attribute when checked
            } else {
                humidityContainer.style.display = 'none';
                humidityValueContainer.style.display = 'none'; // Hide value
                humiditySlider.disabled = true;
                humiditySlider.value = '0';
                humidityValue.textContent = '0%'; // Reset the value with '%' sign
                humiditySlider.removeAttribute('name'); // Remove name attribute when unchecked
            }
        });
    
        humiditySlider.oninput = function() {
            humidityValue.textContent = this.value + '%'; // Update the value with '%' sign
        }
    
        // Dispatch 'change' event to set initial state
        humidityVisibleToggle.dispatchEvent(new Event('change'));
    });
    
}

{   // Slider Toggle and Value Update: Cloud Coverage
    document.addEventListener('DOMContentLoaded', function() {
        // Slider Toggle and Value Update: Cloud Coverage
        const cloudCoverageVisibleToggle = document.getElementById('cloudCoverageVisibleToggle');
        const cloudCoverageContainer = document.getElementById('cloudCoverageContainer');
        const cloudCoverageSlider = document.getElementById('cloudCoverage');
        const cloudCoverageValue = document.getElementById('cloudCoverageValue');
        const cloudCoverageValueContainer = document.getElementById('cloudCoverageValueContainer'); // Ensure this is the correct ID
    
        cloudCoverageVisibleToggle.addEventListener('change', function() {
            if (this.checked) {
                cloudCoverageContainer.style.display = 'block';
                cloudCoverageValueContainer.style.display = 'block'; // Adjust to inline for a single line
                cloudCoverageSlider.disabled = false;
                cloudCoverageSlider.setAttribute('name', 'cloudCoverage'); // Add name attribute when checked
            } else {
                cloudCoverageContainer.style.display = 'none';
                cloudCoverageValueContainer.style.display = 'none';
                cloudCoverageSlider.disabled = true;
                cloudCoverageSlider.value = '0';
                cloudCoverageValue.textContent = '0%'; // Reset the value with '%' sign
                cloudCoverageSlider.removeAttribute('name'); // Remove name attribute when unchecked
            }
        });
    
        cloudCoverageSlider.oninput = function() {
            cloudCoverageValue.textContent = this.value + '%'; // Update the value with '%' sign
        };
    
        // Dispatch 'change' event to set initial state
        cloudCoverageVisibleToggle.dispatchEvent(new Event('change'));
    });
    
}

{   // Slider Toggle and Value Update: Moon Phase
    document.addEventListener('DOMContentLoaded', function() {
        const moonPhaseVisibleToggle = document.getElementById('moonPhaseVisibleToggle');
        const moonPhaseSlider = document.getElementById('moonPhaseSlider');
        const moonImagePlaceholder = document.querySelector('.moonImagePlaceholder'); // Reference to the placeholder
    
        moonPhaseVisibleToggle.addEventListener('change', function() {
            const moonPhaseFlexContainer = document.querySelector('.moonPhaseFlexContainer');
            if (this.checked) {
                moonPhaseFlexContainer.style.display = 'flex'; // Show the flex container
                moonPhaseLabel.style.display = 'none'; // Hide the label
                moonPhaseImage.style.display = 'block'; // Show the image
                moonImagePlaceholder.style.display = 'none'; // Hide the placeholder when the image is visible
                moonPhaseSlider.disabled = false;
                moonPhaseSlider.setAttribute('name', 'moonPhase'); // Add name attribute when checked
            } else {
                moonPhaseFlexContainer.style.display = 'none'; // Hide the flex container
                moonPhaseLabel.style.display = 'block'; // Show the label
                moonPhaseImage.style.display = 'none'; // Hide the image
                moonImagePlaceholder.style.display = 'block'; // Show the placeholder when the image is hidden
                moonPhaseSlider.disabled = true;
                moonPhaseSlider.removeAttribute('name'); // Remove name attribute when unchecked
            }
        });
    
        moonPhaseSlider.oninput = function() {
            document.getElementById('moonPhaseImage').src = `/static/moon_images/${this.value}.svg`;
        };
    
        // Dispatch 'change' event to set initial state
        moonPhaseVisibleToggle.dispatchEvent(new Event('change'));
    });
    
}

{   // 'notes' textarea auto expand
    document.addEventListener('DOMContentLoaded', function() {
        const textareas = document.querySelectorAll('textarea.auto-expand');
    
        textareas.forEach(function(textarea) {
            textarea.addEventListener('input', function() {
                this.style.height = 'auto';
                this.style.height = (this.scrollHeight + 2) + 'px'; // Add a small buffer
            });
    
            // Trigger the input event to calculate initial height
            textarea.dispatchEvent(new Event('input'));
        });
    });
}




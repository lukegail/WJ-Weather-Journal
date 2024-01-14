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
    const humidityVisibleToggle = document.getElementById('humidityVisibleToggle');
    const humidityContainer = document.getElementById('humidityContainer');
    const humiditySlider = document.getElementById('humidity');
    const humidityValue = document.getElementById('humidityValue');

    humidityVisibleToggle.addEventListener('change', function() {
        if (this.checked) {
            humidityContainer.style.display = 'block'; // Adjust to inline for a single line
            humidityValueContainer.style.display = 'block'; // Show value
            humiditySlider.disabled = false;
        } else {
            humidityContainer.style.display = 'none';
            humidityValueContainer.style.display = 'none'; // Hide value
            humiditySlider.disabled = true;
            humiditySlider.value = '0';
            humidityValue.textContent = '0%'; // Reset the value with '%' sign
        }
    });

    humiditySlider.oninput = function() {
        humidityValue.textContent = this.value + '%'; // Update the value with '%' sign
    }
}

{   // Slider Toggle and Value Update: Cloud Coverage
    const cloudCoverageVisibleToggle = document.getElementById('cloudCoverageVisibleToggle');
    const cloudCoverageContainer = document.getElementById('cloudCoverageContainer');
    const cloudCoverageSlider = document.getElementById('cloudCoverage');
    const cloudCoverageValue = document.getElementById('cloudCoverageValue');

    cloudCoverageVisibleToggle.addEventListener('change', function() {
        if (this.checked) {
            cloudCoverageContainer.style.display = 'block';
            cloudCoverageValueContainer.style.display = 'block'; // Adjust to inline for a single line
            cloudCoverageSlider.disabled = false;
        } else {
            cloudCoverageContainer.style.display = 'none';
            cloudCoverageValueContainer.style.display = 'none';
            cloudCoverageSlider.disabled = true;
            cloudCoverageSlider.value = '0';
            cloudCoverageValue.textContent = '0%'; // Reset the value with '%' sign
        }
    });

    cloudCoverageSlider.oninput = function() {
        cloudCoverageValue.textContent = this.value + '%'; // Update the value with '%' sign
    }
}

{   // Slider Toggle and Value Update: Moon Phase
    const moonPhaseVisibleToggle = document.getElementById('moonPhaseVisibleToggle');
    const moonPhaseContainer = document.getElementById('moonPhaseContainer');
    const moonPhaseSlider = document.getElementById('moonPhase');
    const moonPhaseValue = document.getElementById('moonPhaseValue');

    moonPhaseVisibleToggle.addEventListener('change', function() {
        if (this.checked) {
            moonPhaseContainer.style.display = 'block';
            moonPhaseValueContainer.style.display = 'block'; // Adjust to inline for a single line
            moonPhaseSlider.disabled = false;
        } else {
            moonPhaseContainer.style.display = 'none';
            moonPhaseValueContainer.style.display = 'none'; // Show label when unchecked
            moonPhaseSlider.disabled = true;
            moonPhaseSlider.value = '1';
        }
    });

    moonPhaseSlider.oninput = function() {
        moonPhaseValue.textContent = this.value;
    }
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




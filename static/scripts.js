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
            humidityLabel.style.display = 'none';
            humidityContainer.style.display = 'inline'; // Adjust to inline for a single line
            humiditySlider.disabled = false;
        } else {
            humidityLabel.style.display = 'inline'; // Show label when unchecked
            humidityContainer.style.display = 'none';
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
    const cloudVisibleToggle = document.getElementById('cloudVisibleToggle');
    const cloudContainer = document.getElementById('cloudContainer');
    const cloudCoverageSlider = document.getElementById('cloudCoverage');
    const cloudValue = document.getElementById('cloudValue');

    cloudVisibleToggle.addEventListener('change', function() {
        if (this.checked) {
            cloudCoverageLabel.style.display = 'none';
            cloudContainer.style.display = 'inline'; // Adjust to inline for a single line
            cloudCoverageSlider.disabled = false;
        } else {
            cloudCoverageLabel.style.display = 'inline'; // Show label when unchecked
            cloudContainer.style.display = 'none';
            cloudCoverageSlider.disabled = true;
            cloudCoverageSlider.value = '0';
            cloudValue.textContent = '0%'; // Reset the value with '%' sign
        }
    });

    cloudCoverageSlider.oninput = function() {
        cloudValue.textContent = this.value + '%'; // Update the value with '%' sign
    }
}

{   // Slider Toggle and Value Update: Moon Phase
    const moonVisibleToggle = document.getElementById('moonVisibleToggle');
    const moonPhaseContainer = document.getElementById('moonPhaseContainer');
    const moonPhaseSlider = document.getElementById('moonPhase');
    const moonPhaseValue = document.getElementById('moonPhaseValue');

    moonVisibleToggle.addEventListener('change', function() {
        if (this.checked) {
            moonLabel.style.display = 'none';
            moonPhaseContainer.style.display = 'inline'; // Adjust to inline for a single line
            moonPhaseSlider.disabled = false;
        } else {
            moonLabel.style.display = 'inline'; // Show label when unchecked
            moonPhaseContainer.style.display = 'none';
            moonPhaseSlider.disabled = true;
            moonPhaseSlider.value = '1';
        }
    });

    moonPhaseSlider.oninput = function() {
        moonPhaseValue.textContent = this.value;
    }
}

{   // 'notes' textarea auto expand
    const textarea = document.querySelector('textarea.auto-expand');
    textarea.addEventListener('input', function() {
        this.style.height = 'auto';
        this.style.height = (this.scrollHeight) + 'px';
    });
}




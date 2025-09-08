// Global Map JavaScript for Jiarong Guo's Personal Website
// This script creates an interactive map showing research locations and collaborations

function initGlobalMap() {
    // Map center (Hong Kong)
    const center = {lat: 22.3193, lng: 114.1694};
    
    // Initialize the map
    const map = new google.maps.Map(document.getElementById('global-map'), {
        zoom: 3,
        center: center,
        mapTypeId: 'terrain',
        styles: [
            {
                featureType: 'water',
                elementType: 'geometry',
                stylers: [{color: '#e9e9e9'}, {lightness: 17}]
            },
            {
                featureType: 'landscape',
                elementType: 'geometry',
                stylers: [{color: '#f5f5f5'}, {lightness: 20}]
            }
        ]
    });

    // Research locations data
    const locations = [
        {
            lat: 22.3193,
            lng: 114.1694,
            title: 'Hong Kong, China',
            content: `
                <div style="max-width: 300px;">
                    <h3 style="margin: 0 0 10px 0; color: #2c3e50;">Hong Kong, China</h3>
                    <p style="margin: 5px 0;"><strong>Institution:</strong> Current research base</p>
                    <p style="margin: 5px 0;"><strong>Activities:</strong> Medical image analysis research, computer vision projects</p>
                    <p style="margin: 5px 0;"><strong>Duration:</strong> Current</p>
                    <p style="margin: 5px 0;"><strong>Research Focus:</strong> AI in healthcare, medical imaging</p>
                </div>
            `,
            icon: {
                url: 'https://maps.google.com/mapfiles/ms/icons/red-dot.png'
            }
        },
        {
            lat: 39.9042,
            lng: 116.4074,
            title: 'Beijing, China',
            content: `
                <div style="max-width: 300px;">
                    <h3 style="margin: 0 0 10px 0; color: #2c3e50;">Beijing, China</h3>
                    <p style="margin: 5px 0;"><strong>Institution:</strong> Research collaborations</p>
                    <p style="margin: 5px 0;"><strong>Activities:</strong> Academic conferences, research meetings</p>
                    <p style="margin: 5px 0;"><strong>Duration:</strong> Various periods</p>
                    <p style="margin: 5px 0;"><strong>Focus:</strong> Medical AI research collaborations</p>
                </div>
            `,
            icon: {
                url: 'https://maps.google.com/mapfiles/ms/icons/blue-dot.png'
            }
        },
        {
            lat: 31.2304,
            lng: 121.4737,
            title: 'Shanghai, China',
            content: `
                <div style="max-width: 300px;">
                    <h3 style="margin: 0 0 10px 0; color: #2c3e50;">Shanghai, China</h3>
                    <p style="margin: 5px 0;"><strong>Institution:</strong> Conference presentations</p>
                    <p style="margin: 5px 0;"><strong>Activities:</strong> Medical imaging conferences, research presentations</p>
                    <p style="margin: 5px 0;"><strong>Duration:</strong> Conference periods</p>
                    <p style="margin: 5px 0;"><strong>Focus:</strong> Medical imaging technology</p>
                </div>
            `,
            icon: {
                url: 'https://maps.google.com/mapfiles/ms/icons/green-dot.png'
            }
        },
        {
            lat: 35.6762,
            lng: 139.6503,
            title: 'Tokyo, Japan',
            content: `
                <div style="max-width: 300px;">
                    <h3 style="margin: 0 0 10px 0; color: #2c3e50;">Tokyo, Japan</h3>
                    <p style="margin: 5px 0;"><strong>Institution:</strong> International conferences</p>
                    <p style="margin: 5px 0;"><strong>Activities:</strong> Computer vision conferences, research collaborations</p>
                    <p style="margin: 5px 0;"><strong>Duration:</strong> Conference periods</p>
                    <p style="margin: 5px 0;"><strong>Focus:</strong> Computer vision and AI</p>
                </div>
            `,
            icon: {
                url: 'https://maps.google.com/mapfiles/ms/icons/yellow-dot.png'
            }
        },
        {
            lat: 1.3521,
            lng: 103.8198,
            title: 'Singapore',
            content: `
                <div style="max-width: 300px;">
                    <h3 style="margin: 0 0 10px 0; color: #2c3e50;">Singapore</h3>
                    <p style="margin: 5px 0;"><strong>Institution:</strong> Research collaborations</p>
                    <p style="margin: 5px 0;"><strong>Activities:</strong> Medical AI conferences, research meetings</p>
                    <p style="margin: 5px 0;"><strong>Duration:</strong> Various periods</p>
                    <p style="margin: 5px 0;"><strong>Focus:</strong> Medical AI and healthcare technology</p>
                </div>
            `,
            icon: {
                url: 'https://maps.google.com/mapfiles/ms/icons/purple-dot.png'
            }
        },
        {
            lat: 37.7749,
            lng: -122.4194,
            title: 'San Francisco, USA',
            content: `
                <div style="max-width: 300px;">
                    <h3 style="margin: 0 0 10px 0; color: #2c3e50;">San Francisco, USA</h3>
                    <p style="margin: 5px 0;"><strong>Institution:</strong> Tech conferences</p>
                    <p style="margin: 5px 0;"><strong>Activities:</strong> AI/ML conferences, research presentations</p>
                    <p style="margin: 5px 0;"><strong>Duration:</strong> Conference periods</p>
                    <p style="margin: 5px 0;"><strong>Focus:</strong> AI and machine learning technologies</p>
                </div>
            `,
            icon: {
                url: 'https://maps.google.com/mapfiles/ms/icons/orange-dot.png'
            }
        },
        {
            lat: 51.5074,
            lng: -0.1278,
            title: 'London, UK',
            content: `
                <div style="max-width: 300px;">
                    <h3 style="margin: 0 0 10px 0; color: #2c3e50;">London, UK</h3>
                    <p style="margin: 5px 0;"><strong>Institution:</strong> International conferences</p>
                    <p style="margin: 5px 0;"><strong>Activities:</strong> Medical imaging conferences, research collaborations</p>
                    <p style="margin: 5px 0;"><strong>Duration:</strong> Conference periods</p>
                    <p style="margin: 5px 0;"><strong>Focus:</strong> Medical imaging and healthcare AI</p>
                </div>
            `,
            icon: {
                url: 'https://maps.google.com/mapfiles/ms/icons/pink-dot.png'
            }
        }
    ];

    // Create markers and info windows
    const infoWindows = [];
    
    locations.forEach((location, index) => {
        const marker = new google.maps.Marker({
            position: {lat: location.lat, lng: location.lng},
            map: map,
            title: location.title,
            icon: location.icon
        });

        const infoWindow = new google.maps.InfoWindow({
            content: location.content
        });

        infoWindows.push(infoWindow);

        // Add click event listener
        marker.addListener('click', () => {
            // Close all other info windows
            infoWindows.forEach(window => window.close());
            // Open this info window
            infoWindow.open(map, marker);
        });

        // Add hover effect
        marker.addListener('mouseover', () => {
            marker.setAnimation(google.maps.Animation.BOUNCE);
            setTimeout(() => {
                marker.setAnimation(null);
            }, 750);
        });
    });

    // Add map controls
    const controlDiv = document.createElement('div');
    controlDiv.style.marginTop = '10px';
    controlDiv.style.marginLeft = '10px';
    
    const controlButton = document.createElement('button');
    controlButton.innerHTML = 'Reset View';
    controlButton.style.padding = '8px 16px';
    controlButton.style.backgroundColor = '#2c3e50';
    controlButton.style.color = 'white';
    controlButton.style.border = 'none';
    controlButton.style.borderRadius = '4px';
    controlButton.style.cursor = 'pointer';
    controlButton.style.fontSize = '14px';
    
    controlButton.addEventListener('click', () => {
        map.setCenter(center);
        map.setZoom(3);
        infoWindows.forEach(window => window.close());
    });
    
    controlDiv.appendChild(controlButton);
    map.controls[google.maps.ControlPosition.TOP_LEFT].push(controlDiv);
}

// Initialize map when page loads
document.addEventListener('DOMContentLoaded', function() {
    // Check if Google Maps is loaded
    if (typeof google !== 'undefined' && google.maps) {
        initGlobalMap();
    } else {
        // Load Google Maps API if not already loaded
        const script = document.createElement('script');
        script.src = 'https://maps.googleapis.com/maps/api/js?key=AIzaSyBFw0Qbyq9zTFTd-tUY6dOWWgUjJqoUzYc&callback=initGlobalMap';
        script.async = true;
        script.defer = true;
        document.head.appendChild(script);
    }
});
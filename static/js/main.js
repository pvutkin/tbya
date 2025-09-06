// Main JavaScript file for the TBYA portal

document.addEventListener('DOMContentLoaded', function() {
    // Initialize any common functionality
    
    // Handle click events for job applications and course enrollments
    document.addEventListener('click', function(e) {
        // Job application button
        if (e.target.matches('.apply-btn')) {
            const jobId = e.target.dataset.jobId;
            if (jobId) {
                // Send analytics event
                sendAnalyticsEvent('job_application', jobId, null);
            }
        }
        
        // Course enrollment button
        if (e.target.matches('.enroll-btn')) {
            const courseId = e.target.dataset.courseId;
            if (courseId) {
                // Send analytics event
                sendAnalyticsEvent('course_enrollment', null, courseId);
            }
        }
    });
    
    // Function to send analytics events
    function sendAnalyticsEvent(clickType, jobId, courseId) {
        fetch('/analytics/track/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': getCookie('csrftoken')
            },
            body: JSON.stringify({
                click_type: clickType,
                job_id: jobId,
                course_id: courseId,
                ip_address: null, // Will be filled by backend
                user_agent: navigator.userAgent
            })
        })
        .then(response => response.json())
        .then(data => {
            console.log('Analytics event sent:', data);
        })
        .catch(error => {
            console.error('Error sending analytics event:', error);
        });
    }
    
    // Helper function to get cookie value
    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
});
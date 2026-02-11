import React, { useEffect, useState } from 'react';

const Activities = () => {
  const [activities, setActivities] = useState([]);
  const endpoint = `https://${process.env.REACT_APP_CODESPACE_NAME}-8000.app.github.dev/api/activities/`;

  useEffect(() => {
    fetch(endpoint)
      .then(res => res.json())
      .then(data => {
        const items = data.results || data;
        setActivities(items);
        console.log('Fetched activities:', items);
        console.log('Endpoint:', endpoint);
      })
      .catch(err => console.error('Error fetching activities:', err));
  }, [endpoint]);

  return (
    <div className="container mt-4">
      <h2>Activities</h2>
      <ul className="list-group">
        {activities.map((a, i) => (
          <li key={i} className="list-group-item">
            {a.user_email} - {a.type} ({a.date})
          </li>
        ))}
      </ul>
    </div>
  );
};

export default Activities;

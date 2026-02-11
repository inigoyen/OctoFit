import React, { useEffect, useState } from 'react';

const Teams = () => {
  const [teams, setTeams] = useState([]);
  const endpoint = `https://${process.env.REACT_CODESPACE_NAME}-8000.app.github.dev/api/teams/`;

  useEffect(() => {
    fetch(endpoint)
      .then(res => res.json())
      .then(data => {
        const items = data.results || data;
        setTeams(items);
        console.log('Fetched teams:', items);
        console.log('Endpoint:', endpoint);
      })
      .catch(err => console.error('Error fetching teams:', err));
  }, [endpoint]);

  return (
    <div className="container mt-4">
      <h2>Teams</h2>
      <ul className="list-group">
        {teams.map((t, i) => (
          <li key={i} className="list-group-item">
            {t.name} - {t.description}
          </li>
        ))}
      </ul>
    </div>
  );
};

export default Teams;

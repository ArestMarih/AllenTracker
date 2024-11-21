import { useState, useEffect } from "react";

import "./App.css";
import TaskCard from "./TaskCard";

function App() {
  const [data, setData] = useState([]);
  const getApiData = async () => {
    const resp = await fetch("http://127.0.0.1:8000/api/v1/task").then((resp) =>
      resp.json()
    );
    setData(resp.task);
  };
  useEffect(() => {
    getApiData();
  }, []);
  return (
    <>
      <div>
        {data.map((i) => (
          <TaskCard i={i} key={i.id} />
        ))}
      </div>
    </>
  );
}

export default App;

import React from "react";
import axios from "axios";

const SetDone = ({ id }) => {
  async function subForm(e) {
    e.preventDefault();
    await axios.put(`http://127.0.0.1:8000/api/v1/task/${id}`);
  }
  return (
    <div>
      <form onSubmit={subForm}>
        <button type="submit">Выполнено</button>
      </form>
    </div>
  );
};

export default SetDone;

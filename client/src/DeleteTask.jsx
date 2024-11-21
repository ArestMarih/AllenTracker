import React from "react";
import axios from "axios";

const DeleteTask = ({ id }) => {
  async function subForm(e) {
    e.preventDefault();
    await axios.delete(`http://127.0.0.1:8000/api/v1/task/${id}`);
  }
  return (
    <div>
      <form onSubmit={subForm}>
        <button type="submit">Удалить</button>
      </form>
    </div>
  );
};

export default DeleteTask;

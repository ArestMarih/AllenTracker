import React from "react";
import DeleteTask from "./DeleteTask";
import SetDone from "./SetDone";

const TaskCard = ({ i }) => {
  return (
    <div>
      <div id={i.id}>
        <div id="title">
          <span>{i.title}</span>
        </div>
        <div id="desc">
          <span>{i.desc}</span>
        </div>
        <div id="exp">
          <span>{i.exp}</span>
        </div>
        <div id="done">
          <span>{!i.done && <p>Не выполнено</p>}</span>
          <span>{i.done && <p>Выполнено</p>}</span>
        </div>
        <DeleteTask id={i.id} />
        {!i.done && <SetDone id={i.id} />}
      </div>
    </div>
  );
};

export default TaskCard;

import React from "react";
import App from "./App";
import ReactDOM from "react-dom";

import DataTable from "../../components/DataTable";

ReactDOM.render(<App />, document.getElementById("root"));


function App() {
    return (
        <div>
            <DataTable />
            <h1>Holaaa</h1>
        </div>
    );
}

export default App;

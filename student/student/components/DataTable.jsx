import React, { useEffect, useState } from "react";
import axios from "axios";

const DataTable = () => {
    const [data, setData] = useState([]);
    const [loading, setLoading] = useState(true);

    useEffect(() => {
        // Consumir la API
        const fetchData = async () => {
            try {
                const response = await axios.get("http://localhost:8000/api/datos/");
                setData(response.data);
            } catch (error) {
                console.error("Error fetching data:", error);
            } finally {
                setLoading(false);
            }
        };

        fetchData();
    }, []);

    if (loading) {
        return <p>Loading...</p>;
    }

    return (
        <div>
            <table border="1" id="tabla-datos">
                <thead>
                    <tr>
                        <th>#</th>
                        <th>Código</th>
                        <th>Nombres y Apellidos</th>
                        <th>Corte 1</th>
                        <th>Corte 2</th>
                        <th>Corte 3</th>
                        <th>Nota Final</th>
                        <th>Habilitación</th>
                        <th>Faltas</th>
                    </tr>
                </thead>
                <tbody>
                        {data.map((item) => (
                            <tr key={item.id}>
                                <td>{item.codigo}</td>
                                <td>{item.nombre}</td>
                                <td>{item.email}</td>
                            </tr>
                        ))}
                </tbody>
            </table>
        </div>
    );
};

export default DataTable;
ReactDOM.render(<App />, document.getElementById("root"));

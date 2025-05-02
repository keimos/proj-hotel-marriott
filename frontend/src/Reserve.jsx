import { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import axios from 'axios';

function Reserve() {
    const [form, setForm] = useState({
        guest_name: "",
        room_type: "",
        check_in: "",
        check_out: ""
    });

    const navigate = useNavigate();

    const handleChange = (e) => {
      setForm({ ...form, [e.target.name]: e.target.value });
    };

    const handleSubmit = async (e) => {
        e.preventDefault();
        try {
            await axios.post("http://localhst:5000/reserve", form);
            navigate("/success");
        } catch (error) {
            console.error("There was an error making the reservation!", error);
            navigate("/error");
        }
    };

    return ();
}

export default Reserve;
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

    const handleSubmit = async (e) => {
        e.preventDefault();
        try {
            await
            navigate("/success");
        } catch (error) {
            console.error("There was an error making the reservation!", error);
            navigate("/error");
        }
    };

    
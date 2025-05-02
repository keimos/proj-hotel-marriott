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

    return (
        <div className="container">
            <h2>Reserve a Room</h2>
            <form onSubmit={handleSubmit}>
                <div className="mb-3">
                    <label htmlFor="guest_name" className="form-label">Guest Name</label>
                    <input type="text" className="form-control" id="guest_name" name="guest_name" value={form.guest_name} onChange={handleChange} required />
                </div>
                <div className="mb-3">
                    <label htmlFor="room_type" className="form-label">Room Type</label>
                    <input type="text" className="form-control" id="room_type" name="room_type" value={form.room_type} onChange={handleChange} required />
                </div>
                <div className="mb-3">
                    <label htmlFor="check_in" className="form-label">Check-in Date</label>
                    <input type="date" className="form-control" id="check_in" name="check_in" value={form.check_in} onChange={handleChange} required />
                </div>
                <div className="mb-3">
                    <label htmlFor="check_out" className="form-label">Check-out Date</label>
                    <input type="date" className="form-control" id="check_out" name="check_out" value={form.check_out} onChange={handleChange} required />
                </div>
                <button type="submit" className="btn btn-primary">Reserve</button>
            </form>
        </div>
    );
}

export default Reserve;
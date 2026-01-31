import { useState, useEffect } from 'react';
import './App.css';
import React from 'react';
import axios from 'axios';

function App(){
  const [students, setStudents] = useState([]);
  const [form, setForm] = useState({
    first_name: '',
    last_name: '',
    address: '',
    pincode: '',
    city: '',
    state: '',
    father_name: '',
    mother_name: '',
    phno: '',
    emailid: '',
    adhaar_no: ''
  });

  useEffect(() => {
    loadData();
  }, []);

  const loadData = () => {
    axios.get('http://localhost:8000/rect/')
      .then((response) => {
        setStudents(response.data);
      })
      .catch((error) => console.error('Error fetching students:', error));
  };

  const submit = () => {
    axios.post('http://localhost:8000/rect/', form)
      .then(() => {
        loadData();
        setForm({
          first_name: '',
          last_name: '',
          address: '',
          pincode: '',
          city: '',
          state: '',
          father_name: '',
          mother_name: '',
          phno: '',
          emailid: '',
          adhaar_no: ''
        });
      })
      .catch((error) => console.error('Error submitting form:', error));
  };

  const deleteStudent = (id) => {
    axios.delete(`http://localhost:8000/rect/${id}/`)
      .then(() => loadData())
      .catch((error) => console.error('Error deleting student:', error));
  };

  return (
    <div style={{ padding: 30 }}>
      <h2>Student Dashboard</h2>
      
      <h3>Add New Student</h3>
      <input placeholder="First Name" value={form.first_name} onChange={(e) => setForm({...form, first_name: e.target.value})} /><br/><br/>
      <input placeholder="Last Name" value={form.last_name} onChange={(e) => setForm({...form, last_name: e.target.value})} /><br/><br/>
      <input placeholder="Address" value={form.address} onChange={(e) => setForm({...form, address: e.target.value})} /><br/><br/>
      <input placeholder="Pincode" value={form.pincode} onChange={(e) => setForm({...form, pincode: e.target.value})} /><br/><br/>
      <input placeholder="City" value={form.city} onChange={(e) => setForm({...form, city: e.target.value})} /><br/><br/>
      <input placeholder="State" value={form.state} onChange={(e) => setForm({...form, state: e.target.value})} /><br/><br/>
      <input placeholder="Father Name" value={form.father_name} onChange={(e) => setForm({...form, father_name: e.target.value})} /><br/><br/>
      <input placeholder="Mother Name" value={form.mother_name} onChange={(e) => setForm({...form, mother_name: e.target.value})} /><br/><br/>
      <input placeholder="Phone" value={form.phno} onChange={(e) => setForm({...form, phno: e.target.value})} /><br/><br/>
      <input placeholder="Email" value={form.emailid} onChange={(e) => setForm({...form, emailid: e.target.value})} /><br/><br/>
      <input placeholder="Adhaar No" value={form.adhaar_no} onChange={(e) => setForm({...form, adhaar_no: e.target.value})} /><br/><br/>
      <button onClick={submit}>Submit</button>
      
      <hr/>
      
      <h3>Student List</h3>
      <table border="1" cellPadding="10" style={{ borderCollapse: 'collapse', width: '100%' }}>
        <thead>
          <tr>
            <th>First Name</th>
            <th>Last Name</th>
            <th>Address</th>
            <th>Pincode</th>
            <th>City</th>
            <th>State</th>
            <th>Father</th>
            <th>Mother</th>
            <th>Phone</th>
            <th>Email</th>
            <th>Adhaar</th>
            <th>Delete</th>
          </tr>
        </thead>
        <tbody>
          {students.map((student) => (
            <tr key={student.id}>
              <td>{student.first_name}</td>
              <td>{student.last_name}</td>
              <td>{student.address}</td>
              <td>{student.pincode}</td>
              <td>{student.city}</td>
              <td>{student.state}</td>
              <td>{student.father_name}</td>
              <td>{student.mother_name}</td>
              <td>{student.phno}</td>
              <td>{student.emailid}</td>
              <td>{student.adhaar_no}</td>
              <td><button onClick={() => deleteStudent(student.id)}>Delete</button></td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default App;

// function App() {
//   const [students, setStudents] = useState([]);
//   const [formData, setFormData] = useState({
//     first_name: '',
//     last_name: '',
//     address: '',
//     pincode: '',
//     city: '',
//     state: '',
//     father_name: '',
//     mother_name: '',
//     phno: '',
//     emailid: '',
//     adhaar_no: ''
//   });

//   useEffect(() => {
//     // Fetch students from Django API
//     fetch('http://localhost:8000/rect/')
//       .then(response => response.json())
//       .then(data => setStudents(data))
//       .catch(error => console.error('Error fetching students:', error));
//   }, []);

//   const handleInputChange = (e) => {
//     const { name, value } = e.target;
//     setFormData(prevState => ({
//       ...prevState,
//       [name]: value
//     }));
//   };

//   const handleSubmit = (e) => {
//     e.preventDefault();
    
//     // Post data to Django API
//     fetch('http://localhost:8000/rect/', {
//       method: 'POST',
//       headers: {
//         'Content-Type': 'application/json',
//       },
//       body: JSON.stringify(formData)
//     })
//       .then(response => response.json())
//       .then(data => {
//         setStudents([...students, data]);
//         setFormData({
//           first_name: '',
//           last_name: '',
//           address: '',
//           pincode: '',
//           city: '',
//           state: '',
//           father_name: '',
//           mother_name: '',
//           phno: '',
//           emailid: '',
//           adhaar_no: ''
//         });
//         alert('Student added successfully!');
//       })
//       .catch(error => {
//         console.error('Error adding student:', error);
//         alert('Error adding student. Please check the console for details.');
//       });
//   };

//   const handleDelete = (id) => {
//     if (window.confirm('Are you sure you want to delete this student?')) {
//       fetch(`http://localhost:8000/rect/${id}/`, {
//         method: 'DELETE',
//       })
//         .then(() => setStudents(students.filter(s => s.id !== id)))
//         .catch(error => console.error('Error deleting student:', error));
//     }
//   };

//   return (
//     <>
//       <nav>
//         <ul>
//           <li>home</li>
//           <li>about</li>
//           <li>contact</li>
//         </ul>
//       </nav>
//       <h1>Welcome to React</h1>
      
//       {/* Form Section */}
//       <div className="form-container">
//         <h2>Add New Student</h2>
//         <form onSubmit={handleSubmit}>
//           <div className="form-row">
//             <div className="form-group">
//               <label htmlFor="first_name">First Name:</label>
//               <input
//                 type="text"
//                 id="first_name"
//                 name="first_name"
//                 value={formData.first_name}
//                 onChange={handleInputChange}
//                 required
//               />
//             </div>
//             <div className="form-group">
//               <label htmlFor="last_name">Last Name:</label>
//               <input
//                 type="text"
//                 id="last_name"
//                 name="last_name"
//                 value={formData.last_name}
//                 onChange={handleInputChange}
//                 required
//               />
//             </div>
//             <div className="form-group">
//               <label htmlFor="address">Address:</label>
//               <input
//                 type="text"
//                 id="address"
//                 name="address"
//                 value={formData.address}
//                 onChange={handleInputChange}
//               />
//             </div>
//           </div>

//           <div className="form-row">
//             <div className="form-group">
//               <label htmlFor="pincode">Pincode:</label>
//               <input
//                 type="text"
//                 id="pincode"
//                 name="pincode"
//                 value={formData.pincode}
//                 onChange={handleInputChange}
//               />
//             </div>
//             <div className="form-group">
//               <label htmlFor="city">City:</label>
//               <input
//                 type="text"
//                 id="city"
//                 name="city"
//                 value={formData.city}
//                 onChange={handleInputChange}
//               />
//             </div>
//             <div className="form-group">
//               <label htmlFor="state">State:</label>
//               <input
//                 type="text"
//                 id="state"
//                 name="state"
//                 value={formData.state}
//                 onChange={handleInputChange}
//               />
//             </div>
//           </div>

//           <div className="form-row">
//             <div className="form-group">
//               <label htmlFor="father_name">Father Name:</label>
//               <input
//                 type="text"
//                 id="father_name"
//                 name="father_name"
//                 value={formData.father_name}
//                 onChange={handleInputChange}
//               />
//             </div>
//             <div className="form-group">
//               <label htmlFor="mother_name">Mother Name:</label>
//               <input
//                 type="text"
//                 id="mother_name"
//                 name="mother_name"
//                 value={formData.mother_name}
//                 onChange={handleInputChange}
//               />
//             </div>
//             <div className="form-group">
//               <label htmlFor="phno">Phone:</label>
//               <input
//                 type="text"
//                 id="phno"
//                 name="phno"
//                 value={formData.phno}
//                 onChange={handleInputChange}
//               />
//             </div>
//           </div>

//           <div className="form-row">
//             <div className="form-group">
//               <label htmlFor="emailid">Email:</label>
//               <input
//                 type="email"
//                 id="emailid"
//                 name="emailid"
//                 value={formData.emailid}
//                 onChange={handleInputChange}
//               />
//             </div>
//             <div className="form-group">
//               <label htmlFor="adhaar_no">Adhaar No:</label>
//               <input
//                 type="text"
//                 id="adhaar_no"
//                 name="adhaar_no"
//                 value={formData.adhaar_no}
//                 onChange={handleInputChange}
//               />
//             </div>
//           </div>

//           <button type="submit" className="submit-btn">Add Student</button>
//         </form>
//       </div>

//       {/* Table Section */}
//       <h2>Student List</h2>
//       <table>
//         <thead>
//           <tr>
//             <th>First Name</th>
//             <th>Last Name</th>
//             <th>Address</th>
//             <th>Pincode</th>
//             <th>City</th>
//             <th>State</th>
//             <th>Father</th>
//             <th>Mother</th>
//             <th>Phone</th>
//             <th>Email</th>
//             <th>Adhaar</th>
//             <th>Actions</th>
//           </tr>
//         </thead>
//         <tbody>
//           {students.map((student) => (
//             <tr key={student.id}>
//               <td>{student.first_name}</td>
//               <td>{student.last_name}</td>
//               <td>{student.address}</td>
//               <td>{student.pincode}</td>
//               <td>{student.city}</td>
//               <td>{student.state}</td>
//               <td>{student.father_name}</td>
//               <td>{student.mother_name}</td>
//               <td>{student.phno}</td>
//               <td>{student.emailid}</td>
//               <td>{student.adhaar_no}</td>
//               <td>
//                 <button onClick={() => handleDelete(student.id)}>Delete</button>
//               </td>
//             </tr>
//           ))}
//         </tbody>
//       </table>
//     </>
//   );
// }

// export default App;
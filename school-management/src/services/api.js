import axios from 'axios';

const apiClient = axios.create({
    baseURL: 'http://127.0.0.1:8000',
    headers:{
        'Content-Type' : 'application/json'
    }
});

export default{
    getStudents(){
        return apiClient.get('/students');
    },

    getStudent(id){
        return apiClient.get(`/students/${id}`);
    },

    createStudent(data){
        return apiClient.post('/students', data);
    },

    updateStudent(id, data){
        return apiClient.put(`/students/${id}`, data);
    },

    deleteStudent(id){
        return apiClient.delete(`/students/${id}`);
    }
};
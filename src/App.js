import React, { useState } from "react";
import { useForm } from "react-hook-form";
import axios from "axios";

const App = () => {
  const { register, handleSubmit } = useForm();
  const [baseimage, setbaseimage] = useState("");
  const uploadLogo = async (data) => {
    console.log(data.target.files);
    const file = data.target.files[0];
    const base64 = await convertBase64(file);
    setbaseimage(base64);
  };
  const convertBase64 = (file) => {
    return new Promise((resolve, reject) => {
      const fileReader = new FileReader();
      fileReader.readAsDataURL(file);
      fileReader.onload = () => {
        resolve(fileReader.result);
      };
      fileReader.onerror = (error) => {
        reject(error);
      };
    });
  };
  const onSubmit = (data2) => {
    console.log("Entered");
    let formData = new FormData();
    // let fileToUpload = data2.image.item(0);
    let fileToUpload2 = data2.file.item(0);
    formData.append("image", baseimage);
    formData.append("file", fileToUpload2, fileToUpload2.name);
    console.log(formData);
    axios
      .post("http://127.0.0.1:8000/api/imageupload/", formData)
      .then((res) => {
        console.log(res);
      })
      .catch((err) => {
        console.log(err);
      });
  };
  return (
    <div>
      <h1>Image Augmentation</h1>
      <div
        className="container"
        style={{ marginTop: "20px", border: "1px solid", padding: "20px" }}
      >
        <form onSubmit={handleSubmit(onSubmit)}>
          <div className="form-group col-md-6">
            <label>Upload Image</label>
            <br />
            <input
              {...register("image")}
              type="file"
              onChange={(data) => {
                uploadLogo(data);
              }}
              accept=".jpg, .jpeg, .bmp, .gif, .png"
            />
          </div>
          <div className="form-group col-md-6">
            <label>Upload XMLFile</label>
            <br />
            <input {...register("file")} type="file" />
          </div>
          <input type="submit" />
        </form>
      </div>
    </div>
  );
};

export default App;

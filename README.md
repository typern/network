# Decentralized Container Management Database on IBM Hyperledger Fabric  

This project implements a decentralized database using IBM Blockchain Technology (Hyperledger Fabric) to manage container transactions. It tracks valuable data such as asset pricing, port transactions, import/export records, and commodity prices. This open-source platform facilitates data sharing between clients, offering insights into key transactions in the logistics and trade industries.

**🏆 Awards**  
- **1st Place (Category)**: IBM Blockchain Technology
- **3rd Place (Global)**: HackMX2018, organized by the Universidad Nacional Autónoma de México.

---

## Features  
- **Decentralized Database**: Ensures transparency and security using Hyperledger Fabric.  
- **Real-time Insights**: Tracks container-related data, including prices and transactions.  
- **Open Source**: Built for collaboration, enabling seamless data sharing across stakeholders.  
- **Modular Architecture**: Separate components for backend (`fabric-dev-server`), database models (`models`), and user interface (`web-app`).

---

## Folder Structure  
- **`fabric-dev-server`**: Contains the Hyperledger Fabric setup and decentralized database.  
- **`models`**: Database schema definitions and interaction logic.  
- **`web-app`**: Frontend interface for interacting with the decentralized system.

---

## Installation  

### Prerequisites  
1. Install **Docker** and **Docker Compose**.  
2. Install **Node.js** (v14 or above).  
3. Clone this repository:  
   ```bash
   git clone https://github.com/your-repo/fabric-container-db.git
   cd fabric-container-db
   ```

---

### Setup  

#### Step 1: Configure Fabric Network  
1. Navigate to the `fabric-dev-server` directory:  
   ```bash
   cd fabric-dev-server
   ```  
2. Start the Fabric network using Docker Compose:  
   ```bash
   ./startFabric.sh
   ```  
3. Install and instantiate the chaincode:  
   ```bash
   ./installChaincode.sh
   ```  

#### Step 2: Set Up Database Models  
1. Move to the `models` directory:  
   ```bash
   cd ../models
   ```  
2. Install dependencies:  
   ```bash
   npm install
   ```  
3. Run database migrations if required:  
   ```bash
   npm run migrate
   ```  

#### Step 3: Run the Web Interface  
1. Navigate to the `web-app` directory:  
   ```bash
   cd ../web-app
   ```  
2. Install dependencies:  
   ```bash
   npm install
   ```  
3. Start the web application:  
   ```bash
   npm start
   ```  

---

## Usage  
1. Access the application at [http://localhost:3000](http://localhost:3000).  
2. Use the web interface to query asset prices, container transactions, and commodity prices.  
3. Shared data will synchronize across all nodes in the Hyperledger Fabric network.  

![alt text gifs](https://github.com/typern/network/blob/master/web-app/public/1.gif)
![alt text gifs](https://github.com/typern/network/blob/master/web-app/public/Peek%202018-09-08%2021-27.gif)
---

## License  
This project is open-source and licensed under the MIT License.  

---  

## Acknowledgments  
This project was created for **HackMX2018**, an innovation hackathon organized by the Universidad Autónoma de México. It earned:  
- **1st Place in its Category**  
- **3rd Place Globally**  

We thank the HackMX2018 organizers and IBM for providing the necessary resources and support.  

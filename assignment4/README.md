# Assignment 4 – Ansible + Flyway + MySQL Deployment
# Step-by-Step Instructions
# Step 1: Start MySQL Container
Using Docker Compose (if provided):
docker-compose up -d
Or use Ansible:
ansible-playbook up.yaml
# Step 2: Run Flyway Migrations
Ensure MySQL is running. Then run this command (single line only):
docker run --rm -v "$(pwd)/flyway/sql":/flyway/sql --network assignment4_default flyway/flyway -url="jdbc:mysql://mysql:3306/testdb?allowPublicKeyRetrieval=true&useSSL=false" -user=root -password=root -locations=filesystem:/flyway/sql migrate
If you get an error about flyway_schema_history, use baseline:
docker run --rm -v "$(pwd)/flyway/sql":/flyway/sql --network assignment4_default flyway/flyway -url="jdbc:mysql://mysql:3306/testdb?allowPublicKeyRetrieval=true&useSSL=false" -user=root -password=root -locations=filesystem:/flyway/sql -baselineOnMigrate=true migrate
# Step 3: Verify Schema with Python Script
Run the test script to verify that all columns exist:
python3 dbtests.py
Expected output: All required columns found ✅
# Step 4: Add a Subscriber (Optional)
Connect to MySQL:
docker exec -it mysql mysql -uroot -proot
Run:

USE testdb;
INSERT INTO subscribers (name, email) VALUES ('Dhyey Patel', 'dhyeypatel9640@gmail.com');
SELECT * FROM subscribers;



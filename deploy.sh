cd frontend
rm -rf dist/
yarn build
cd ..
docker-compose up --build
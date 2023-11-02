import AWS from 'aws-sdk';

AWS.config.update({
	region: 'ap-southeast-1',
	accessKeyId: `${process.env.VITE_APP_AWS_ACCESS_KEY_ID}`,
	secretAccessKey: `${process.env.VITE_APP_AWS_SECRET_ACCESS_KEY}`,
});

const s3 = new AWS.S3({
	// apiVersion: '2006-03-01',
	params: { Bucket: 'bchewy-images' }
});

const uploadImageToS3 = async (file) => {
	const fileName = `planit/${Date.now()}-${file.name}`;
	const params = {
		Key: fileName,
		Body: file,
		ContentType: file.type,
		ACL: 'public-read' // or another appropriate ACL
	};

	try {
		const result = await s3.upload(params).promise();
		console.log('File uploaded successfully', result);
		return result.Location; // returns the file URL
	} catch (error) {
		console.error('File upload failed', error);
		throw error;
	}
}

export default uploadImageToS3;
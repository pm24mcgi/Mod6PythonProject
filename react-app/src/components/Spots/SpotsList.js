import React, { useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
// import { getSpots } from "../../store/spots";

const SpotsList = () => {
	// const dispatch = useDispatch();
	const spots = Object.values(useSelector((state) => state.spot));

	// useEffect(() => {
	// 	let isMounted = true;
	// 	if (isMounted) {
	// 		dispatch(getSpots());
	// 	}
	// 	return () => {
	// 		isMounted = false;
	// 	}
	// }, [dispatch]);

	if (!spots) {
		return <h1>No Spots are being shown</h1>;
	} else {
		return (
			<div>
				<h2>Spots</h2>
				{spots.map((spot) => {
					return (
						<div key={spot.id}>
							<div>Title: {spot.title}</div>
							<div>Description: {spot.description}</div>
							<div>State: {spot.state}</div>
							<div>City: {spot.city}</div>
							<div>Host: {spot.host.username}</div>
							<div>Number of bedrooms: {spot.bedrooms}</div>
							<div>Price per day: ${spot.price_per_day}</div>
							<br />
						</div>
					);
				})}
			</div>
		);
	}
};

export default SpotsList;

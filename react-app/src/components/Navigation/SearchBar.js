import { useState } from "react";
import { BiSearchAlt } from "react-icons/bi";
import { useDispatch, useSelector } from "react-redux";

function SearchBar() {
	const spots = Object.values(useSelector((state) => state.spot));
	const bookings = Object.values(useSelector((state) => state.booking));

	const [bedrooms, setBedrooms] = useState("");
	const [date, setDate] = useState("");
	const [city, setCity] = useState("");
	const [available, setAvailable] = useState(false);

	function getDatesInRange(start_date, end_date) {
		let date = new Date(start_date.getTime());

		const dates = [];

		while (date <= end_date) {
			dates.push(new Date(date));
			date.setDate(date.getDate() + 1);
		}

		return dates;
	}

	function bookingDates(bookingsArr) {
		const dates = [];

		for (let i = 0; i < bookingsArr.length; i++) {
			let booking = bookingsArr[i];
			dates.push(
				...getDatesInRange(
					new Date(booking.start_date),
					new Date(booking.end_date)
				)
			);
		}

		return dates;
	}

	const bookedDates = bookingDates(bookings);
	console.log(bookedDates);

	const isAvailable = (bookedDates, dateInput) => {
		for (const book of bookedDates) {
			console.log(book);
			console.log("dateInput", new Date(dateInput));
			if (book != dateInput) {
				console.log('book != dateInput', book != dateInput)
				setAvailable(true);
			} else {
				setAvailable(false);
			}
		}
		return available;
	};

	const filterSpotGuests = (guests) => {
		// console.log('func',isAvailable(bookedDates, date));
		setAvailable(isAvailable(bookedDates, date));
		console.log('available',available)
		const filteredSpot = spots.filter((spot) => {
			return spot.bedrooms == guests && spot.city == city && available;
		});
		console.log("filteredSpot", filteredSpot);
	};

	return (
		<div className="search-bar-container">
			<div className="search-clicker-container">
				<input
					name="city"
					type="text"
					placeholder="Anywhwere"
					value={city}
					onChange={(e) => setCity(e.target.value)}
				/>
			</div>
			<div className="search-divider"></div>
			<div className="search-clicker-container">
				<input
					name="fromDate"
					type="date"
					placeholder="Any week"
					value={date}
					onChange={(e) => setDate(e.target.value)}
				/>
			</div>
			<div className="search-divider"></div>
			<div className="search-clicker-container">
				<input
					name="guests"
					type="text"
					placeholder="Guests"
					value={bedrooms}
					onChange={(e) => setBedrooms(e.target.value)}
				/>
			</div>
			<div className="search-btn">
				{" "}
				<BiSearchAlt onClick={() => filterSpotGuests(bedrooms)} />{" "}
			</div>
		</div>
	);
}

export default SearchBar;

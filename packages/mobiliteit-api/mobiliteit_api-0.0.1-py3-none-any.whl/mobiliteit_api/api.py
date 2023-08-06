import requests
import datetime



class API():
    def __init__(self, api_key: str, format: str = "json", language: str = "fr"):
        """
        :param api_key (str) -- The API-key to access the API
        :param language (str) [Optional] -- The language the answer should be in
        :return -- None
        """

        self.api_key = None
        self.format = None
        self.language = None

        self.set_api_key(api_key)
        self.set_format(format)
        self.set_language(language)

        

    
    def set_api_key(self, api_key: str) -> None:
        """
        Change the API-Key for accessing the API.

        :param key (str) -- The new API-Key
        """

        if isinstance(api_key, str):
            self.api_key = api_key
        
        else:
            raise TypeError("'api_key' should be of type 'str'!")


    def set_format(self, format: str) -> None:
        """
        Change the output format of the API answer.

        :param format (str) -- The new format [json, xml]
        """
        if isinstance(format, str):
            if format.lower() == "json":
                self.format = "json"
            elif format.lower() == "xml":
                self.format = "xml"
            else:
                raise ValueError(f"'format' should be either 'json' or 'xml', not '{format}'!")
        else:
            raise TypeError("'format' should be of type 'str'!")


    def set_language(self, language: str) -> None:
        """
        Changet the language of the API output.

        :param language (str) -- The new language
        """

        if isinstance(language, str):
            self.language = language
        
        else:
            raise TypeError("'language' should be of type 'str'!")

        

    def get_location_by_coordinate(self, coord_lat: float, coord_long: float, requestId: int = None, jsonpCallback: str = None, radius: int = 100, maxNo: int = 5000, _type: str = None, locationSelectionMode: str = None, products: str = None,
                                meta: str = None, sattributes: str = None, sinfotexts: str = None):
        """
        Searches for stops/stations around the provided coordinate (coord_lat, coord_long).

        :param coord_lat (float) -- The latitude of the centre coordinate
        :param coord_long (float) -- The longitude of the centre coordinate
        :param requestId (int) -- The request ID will be returned in the json/xml response
        :param jsonpCallback (str) -- Requests the JSON response data to be wrapped into a JavaScript function with that name
        :param radius (int) -- The search radius in meter around the given coordinate
        :param maxNo (int) -- The maximum number of returned stops (Range from 1 to 5_000)
        :param _type (str) -- Filter for location types
        :param locationSelectionMode (str) -- Selection mode for locations
        :param products (str) -- Decimal value defining the product classes to be included in the search
        :param meta (str) -- Filter by a predefined meta filter. If the rules of the predefined filter should not be negated, put ! in front of it.
        :param sattributes (str) -- Filter trips by one or more station attribute codes of a journey. Multiple attribute codes are separated by comma. If the attribute should not be part of the be trip, negate it by putting ! in front of it
        :param sinfotexts (str) -- Filter locations by one or more station infotext codes and values. Multiple attribute codes are separated by comma the value by pipe **Has to be updated from documentation once documentation is fixed**

        :return -- locations in the desired output format
        """

        if not isinstance(coord_lat, float) or not isinstance(coord_long, float):
            raise TypeError("Expected coordinates to be of type 'str' !")
        
        params = {
            "originCoordLat": coord_lat,
            "originCoordLong": coord_long,
            "requestId": requestId,
            "jsonpCallback": jsonpCallback,
            "r": radius,
            "maxNo": maxNo,
            "type": _type,
            "locationSelectionMode": locationSelectionMode,
            "products": products,
            "meta": meta,
            "sattributes": sattributes,
            "sinfotexts": sinfotexts,
            "format": self.format,
            "language": self.language
        }

        request = f"https://cdt.hafas.de/opendata/apiserver/location.nearbystops?accessId={self.api_key}"


        ## Only add arguments to the API request which have been provided (= which are not None)
        for argument in params:
            if params[argument] != None:
                add_argument = str("&" + argument + "=" + str(params[argument]))
                request = request + add_argument

        
        answer = self._make_request_(request)

        return answer


    def get_departures(self, station_id: int, requestId: int = None, jsonpCallback: str = None, direction: int = None, date: str = None, time: str = None, 
                        dur: int = None, duration: int = None, maxJourneys: int = None, products: str = None, operators: str = None, lines: str = None, 
                        filterEquiv: str = None, attributes: str = None, platforms: str = None, rtMode: str = "FULL", passlist: str = None):
        """
        Get the departing lines from a stop/station.

        :param station_id (int) -- The id of the stop/station you want to get the departures from
        :param requestId (int) -- The request ID will be returned in the json/xml response
        :param jsonpCallback (str) -- Requests the JSON response data to be wrapped into a JavaScript function with that name
        :param direction (int) -- If only vehicles departing or arriving from a certain direction shall be returned, specify the direction by giving the station/stop ID of the last stop on the journey
        :param date (str) -- Sets the start date for which the departures shall be retrieved. Represented in the format YYYY-MM-DD
        :param time (str) -- Sets the start time for which the departures shall be retrieved. Represented in the format hh:mm[:ss] in 24h nomenclature. Seconds will be ignored for requests
        :param dur (int) -- Range from 0 to 1439 **Needs documentation**
        :param duration (int) -- Set the interval size in minutes. Range from 0 to 1439. Default is 60 **Needs documentation**
        :param maxJourneys (int) -- The maximum number of returned journeys (Range from -1 (=all departing/arriving) to infinity)
        :param products (str) -- Decimal value defining the product classes to be included in the search. It represents a bitmask combining bit number of a product as defined in the HAFAS raw data file zugart **Needs documentation**
        :param operators (str) -- Only journeys provided by the given operators are part of the result. To filter multiple operators, separate the codes by comma. If the operator should not be part of the be trip, negate it by putting ! in front of it. Available operators are: RGTR, AVL, CFL **Missing operators**
        :param lines (str) -- 	Only journeys running the given line are part of the result. To filter multiple lines, separate the codes by comma. If the line should not be part of the be trip, negate it by putting ! in front of it
        :param filterEquiv (str) -- Enables/disables the filtering of equivalent marked stops
        :param attributes (str) -- Filter boards by one or more attribute codes of a journey. Multiple attribute codes are separated by comma. If the attribute should not be part of the result, negate it by putting ! in front of it **Needs documentation**
        :param platforms (str) -- Filter boards by platform. Multiple platforms are separated by comma. Platforms are used for example at train stations. A train station is one single stop but has multiple platforms so the busses stopping there all stop at the same stop (= the train station) but at different platforms. (Depends on the station how many platforms there are.)
        :param rtMode (str) -- Set the realtime mode to be used if enabled. Available are: FULL | For Luxembourg it seems to always return realtime information no matter what you set rtMode to
        :param passlist (str) -- Include a list of all passed waystops? (Is -1 for all waystops and all other numbers for the amount of stops you want?) **Needs documentation**
        """

        if isinstance(station_id, int):
            params = {
                "id": station_id,
                "requestId": requestId, 
                "jsonpCallback": jsonpCallback,
                "direction": direction,
                "date": date,
                "time": time,
                "dur": dur,
                "duration": duration,
                "maxJourneys": maxJourneys,
                "products": products,
                "operators": operators,
                "lines": lines,
                "filterEquiv": filterEquiv,
                "attributes": attributes,
                "platforms": platforms,
                "rtMode": rtMode,
                "passlist": passlist,
                "format": self.format,
                "language": self.language
            }

            request = f"https://cdt.hafas.de/opendata/apiserver/departureBoard?accessId={self.api_key}"


            ## Only add arguments to the API request which have been provided (= which are not None)
            for argument in params:
                if params[argument] != None:
                    add_argument = str("&" + argument + "=" + str(params[argument]))
                    request = request + add_argument

        
            answer = self._make_request_(request)

            return answer

        else:
            raise TypeError("Expected 'station_id' to be of type 'int' !")



    def _make_request_(self, url: str):
        """
        Makes a request to the API.

        :param url (str) -- The request as url

        :return -- The answer of the request (either json or xml)
        """

        if isinstance(url, str):
            response = requests.get(url)

            if self.format == "json":
                json_response = response.json()

                return json_response
            
            else:
                return response
        
        else:
            raise TypeError("'url' should be of type 'str' !")


    
    def calculate_lateness(self, scheduled_time: str, arrival_time: str, output: str = "minutes", timeformat: str = "%H:%M:%S") -> int:
        """
        Calculates the lateness in minutes. \n
        Times are in format "HH:MM:SS" except if you specified otherwise!

        :param scheduled_time (str) -- The time at which the vehicle should have arrived
        :param arrival_time (str) -- The time at which the vehicle actually arrived / will actually arrive
        :param output (str) -- The output format, available are: [seconds, minutes, hours] (minutes and hours will NOT be rounded up/down)
        :param timeformat (str) -- The format in which you provide the scheduled and arribal time

        :return float -- The lateness in the specified time format output (NOT rounded)
        """

        schedtime = datetime.datetime.strptime(scheduled_time, timeformat)
        arrtime = datetime.datetime.strptime(arrival_time, timeformat)

        time_lateness = arrtime - schedtime
        
        if output.lower() == "minutes":
            lateness = time_lateness.seconds / 60
        elif output.lower() == "seconds":
            lateness = time_lateness.seconds
        elif output.lower() == "hours":
            lateness = (time_lateness.seconds / 60) / 60

        else:
            raise ValueError(f"'output' expected one of the following: [seconds, minutes, hours] ; got '{output}' instead!")

        return lateness



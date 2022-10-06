package main

type timeValue struct {
	timestamp int
	value     string
}

type TimeMap struct {
	timeMap map[string][]timeValue
}

func Constructor() TimeMap {
	return TimeMap{timeMap: make(map[string][]timeValue)}
}

func (tm *TimeMap) Set(key string, value string, timestamp int) {
	tm.timeMap[key] = append(tm.timeMap[key], timeValue{
		timestamp: timestamp,
		value:     value,
	})
}

func (tm *TimeMap) Get(key string, timestamp int) string {
	values, ok := tm.timeMap[key]
	if !ok || values[0].timestamp > timestamp {
		return ""
	}

	index := findIndex(values, timestamp)

	return values[index].value
}

func findIndex(values []timeValue, timestamp int) int {
	start := 0
	end := len(values) - 1

	for start <= end {
		mid := (start + end) / 2
		if values[mid].timestamp > timestamp {
			end = mid - 1
		} else {
			start = mid + 1
		}
	}

	return end
}

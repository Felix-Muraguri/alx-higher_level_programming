#!/usr/bin/node
exports.nbOccrrences = function (list, searchElement) {
	return list.reduce((count, current) => current === searchElement ? count + 1 : count, 0);
};

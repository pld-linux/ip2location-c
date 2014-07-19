Summary:	IP2Location C library
Summary(pl.UTF-8):	Biblioteka C IP2Location
Name:		ip2location-c
Version:	6.0.3
Release:	1
License:	LGPL v3+
Group:		Libraries
#Source0Download: http://www.ip2location.com/developers/c
Source0:	http://www.ip2location.com/downloads/%{name}-%{version}.tar.gz
# Source0-md5:	a391adf7fb4e846ffe864d48832714e1
URL:		http://www.ip2location.com/
BuildRequires:	perl-base
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
IP2Location is a C library that enables the user to find the country,
region, city, latitude, longitude, zip code, time zone, ISP, domain
name, connection type, area code, weather, mobile network, elevation,
usage type by IP address or hostname originates from.

%description -l pl.UTF-8
IP2Location to biblioteka C pozwalająca użytkownikowi sprawdzić kraj,
region, miasto, szerokość i długość geograficzną, kod pocztowy, strefę
czasową, dostawcę Internetu, nazwę domenową, rodzaj połączenia, kod
strefy, pogodę, sieć komórkową, wysokość i sposób wykorzystania na
podstawie adresu IP lub nazwy hosta.

%package devel
Summary:	Header files for IP2Location library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki IP2Location
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for IP2Location library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki IP2Location.

%package static
Summary:	Static IP2Location library
Summary(pl.UTF-8):	Statyczna biblioteka IP2Location
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static IP2Location library.

%description static -l pl.UTF-8
Statyczna biblioteka IP2Location.

%package data
Summary:	Free data for IP2Location library
Summary(pl.UTF-8):	Darmowe dane dla biblioteki IP2Location
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description data
Free data for IP2Location library.

%description data -l pl.UTF-8
Darmowe dane dla biblioteki IP2Location.

%prep
%setup -q

%build
%configure

%{__make} -C data convert
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_libdir}/libIP2Location.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libIP2Location.so.1
%dir %{_datadir}/IP2Loc

%files devel
%defattr(644,root,root,755)
%doc Developers_Guide.txt
%attr(755,root,root) %{_libdir}/libIP2Location.so
%{_libdir}/libIP2Location.la
%{_includedir}/IP2Location.h
%{_includedir}/IP2Loc_DBInterface.h

%files static
%defattr(644,root,root,755)
%{_libdir}/libIP2Location.a

%files data
%defattr(644,root,root,755)
%{_datadir}/IP2Loc/IP-COUNTRY.BIN
%{_datadir}/IP2Loc/IPV6-COUNTRY.BIN

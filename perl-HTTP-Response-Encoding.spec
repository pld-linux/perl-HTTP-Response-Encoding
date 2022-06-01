#
# Conditional build:
%bcond_without	tests	# unit tests
#
%define	pdir	HTTP
%define	pnam	Response-Encoding
Summary:	HTTP::Response::Encoding - Adds encoding() to HTTP::Response
Summary(pl.UTF-8):	HTTP::Response::Encoding - dodanie encoding() do HTTP::Response
Name:		perl-HTTP-Response-Encoding
Version:	0.06
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/HTTP/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	7e1d46f2d88022580e1a18bb7ac4ab71
URL:		https://metacpan.org/dist/HTTP-Response-Encoding
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	rpmbuild(macros) >= 1.745
%if %{with tests}
BuildRequires:	perl-Test-Pod >= 1.14
BuildRequires:	perl-Test-Pod-Coverage >= 1.04
BuildRequires:	perl-libwww
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module adds the following methods to HTTP::Response objects:
charset, encoder, encoding.

%description -l pl.UTF-8
Ten moduł dodaje do obiektów HTTP::Response metody: charset, encoder,
encoding.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%dir %{perl_vendorlib}/HTTP/Response
%{perl_vendorlib}/HTTP/Response/Encoding.pm
%{_mandir}/man3/HTTP::Response::Encoding.3pm*

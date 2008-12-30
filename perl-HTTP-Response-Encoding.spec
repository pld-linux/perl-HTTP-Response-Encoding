#
# Conditional build:
%bcond_without	autodeps	# don't BR packages needed only for resolving deps
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	HTTP
%define	pnam	Response-Encoding
Summary:	HTTP::Response::Encoding - Adds encoding() to HTTP::Response
Name:		perl-HTTP-Response-Encoding
Version:	0.05
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/HTTP/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	bb5880687bfb8b1e220c5c3c2b7d1408
URL:		http://search.cpan.org/dist/HTTP-Response-Encoding/
%{?with_tests:BuildRequires:	perl-Test-Pod >= 1.14}
%{?with_tests:BuildRequires:	perl-Test-Pod-Coverage >= 1.04}
BuildRequires:	perl-devel >= 1:5.8.0
%{?with_tests:BuildRequires:	perl-libwww}
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module adds the following methods to HTTP::Response objects.

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
%{_mandir}/man3/*
